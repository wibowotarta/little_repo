# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: GiftPlanner
import unittest
from GiftPlanner import GiftPlanner, Occasion, Recipient, Gift, PurchaseStatus

class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.planner = GiftPlanner()

    def test_add_recipient_no_name(self):
        with self.assertRaises(ValueError):
            self.planner.add_recipient(name=None, email=None)

    def test_add_occasion_no_name(self):
        with self.assertRaises(ValueError):
            self.planner.add_occasion(name=None, code=None)

    def test_add_gift_no_recipient(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Test", occasion_code="birthday")

    def test_add_gift_no_occasion(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Test", recipient_name="John")

    def test_add_purchase_no_gift(self):
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name="Test", status="ordered", note="test")

    def test_add_purchase_no_status(self):
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name="Test", note="test")

    def test_add_purchase_no_note(self):
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name="Test", status="ordered")

    def test_add_purchase_invalid_status(self):
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name="Test", status="invalid", note="test")

    def test_add_gift_no_name(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name=None, occasion_code="birthday")

    def test_add_gift_no_occasion_code(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Test", occasion_code=None)

    def test_add_purchase_no_gift_name(self):
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name=None, status="ordered", note="test")

    def test_add_purchase_no_status_value(self):
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name="Test", status="", note="test")

    def test_add_purchase_no_note_value(self):
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name="Test", status="ordered", note="")

    def test_add_gift_duplicate_recipient(self):
        self.planner.add_recipient(name="Jane", email="jane@example.com")
        self.planner.add_occasion(name="birthday", code="birthday")
        self.planner.add_gift(name="Jewelry", occasion_code="birthday")
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Jewelry2", occasion_code="birthday")

    def test_add_gift_duplicate_occasion(self):
        self.planner.add_recipient(name="Jane", email="jane@example.com")
        self.planner.add_occasion(name="birthday", code="birthday")
        self.planner.add_gift(name="Jewelry", occasion_code="birthday")
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Jewelry2", occasion_code="birthday")

    def test_add_gift_duplicate_name(self):
        self.planner.add_recipient(name="Jane", email="jane@example.com")
        self.planner.add_occasion(name="birthday", code="birthday")
        self.planner.add_gift(name="Jewelry", occasion_code="birthday")
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Jewelry", occasion_code="birthday")

    def test_add_purchase_duplicate_gift(self):
        self.planner.add_recipient(name="Jane", email="jane@example.com")
        self.planner.add_occasion(name="birthday", code="birthday")
        self.planner.add_gift(name="Jewelry", occasion_code="birthday")
        with self.assertRaises(ValueError):
            self.planner.add_purchase(gift_name="Jewelry", status="ordered", note="test")

    def test_add_gift_no_recipient_name(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Test", recipient_name=None)

    def test_add_gift_no_occasion_name(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Test", occasion_name=None)

    def test_add_gift_no_gift_name(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name=None, occasion_code="birthday")

    def test_add_gift_no_gift_occasion_code(self):
        with self.assertRaises(ValueError):
            self.planner.add_gift(name="Test", occasion_code=None)

if __name__ == "__main__":
    unittest.main()
