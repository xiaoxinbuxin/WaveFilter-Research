"""Regression checks for the actual public notebook's evaluation boundaries."""

import json
from pathlib import Path
import unittest

class PublicDemoBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        notebook = Path(__file__).resolve().parents[1] / "notebooks/public_demo.ipynb"
        cells = json.loads(notebook.read_text())["cells"]
        cls.state = {}
        # Execute the real data, feature, label, and split cells, without the
        # later bootstrap/plot/export steps. No copy of the labeling logic.
        for cell in cells:
            if cell["cell_type"] == "code":
                exec("".join(cell["source"]), cls.state)
                if "development" in cls.state and "holdout" in cls.state:
                    break

    def test_unavailable_history_is_not_a_negative_label(self):
        state = self.state
        unavailable = state["future_vol_threshold"].isna()
        self.assertTrue(unavailable.any())
        self.assertTrue(state["df"].loc[unavailable, "future_high_vol"].isna().all())
        evaluated = state["development"].index.union(state["holdout"].index)
        self.assertTrue(evaluated.intersection(state["df"].index[unavailable]).empty)

    def test_partial_future_windows_are_not_evaluated(self):
        state = self.state
        incomplete = state["future_abs"].isna().any(axis=1)
        self.assertTrue(incomplete.any())
        self.assertTrue(state["df"].loc[incomplete, "future_high_vol"].isna().all())
        self.assertTrue(
            state["df"].loc[incomplete, "future_6bar_mean_abs_return"].isna().all()
        )
        evaluated = state["development"].index.union(state["holdout"].index)
        self.assertTrue(evaluated.intersection(state["df"].index[incomplete]).empty)

    def test_development_labels_finish_before_holdout(self):
        state = self.state
        horizon = state["future_abs"].shape[1]
        times = state["df"].index
        for event_time in state["development"].index[-horizon:]:
            label_end = times[times.get_loc(event_time) + horizon]
            self.assertLess(label_end, state["holdout"].index.min())

    def test_complete_label_uses_only_the_next_six_bars(self):
        state = self.state
        frame = state["df"]
        event_time = state["development"].index[10]
        position = frame.index.get_loc(event_time)
        expected = frame["abs_return"].iloc[position + 1:position + 7].mean()
        self.assertAlmostEqual(frame.at[event_time, "future_6bar_mean_abs_return"], expected)

    def test_split_is_ordered_disjoint_and_contains_only_valid_targets(self):
        development = self.state["development"]
        holdout = self.state["holdout"]
        self.assertTrue(development.index.intersection(holdout.index).empty)
        self.assertLess(development.index.max(), holdout.index.min())
        for frame in (development, holdout):
            self.assertTrue(frame.index.is_monotonic_increasing)
            self.assertFalse(frame["future_high_vol"].isna().any())
            self.assertFalse(frame["demo_event"].isna().any())


if __name__ == "__main__":
    unittest.main()
