import unittest

from snips_nlu_metrics.utils.exception import NotEnoughDataError


class TestException(unittest.TestCase):
    def test_not_enough_data_error_repr(self):
        # Given
        dataset = {
            "intents": {
                "intents_1": {
                    "utterances": 5 * [{"data": [{"text": "foobar"}]}]
                },
                "intents_2": {
                    "utterances": 7 * [{"data": [{"text": "foobar"}]}]
                }
            },
            "entities": dict(),
            "language": "en",
        }
        error = NotEnoughDataError(dataset=dataset, nb_folds=4,
                                   train_size_ratio=0.5)

        # When
        repr_error = repr(error)
        error_message = error.message

        # Then
        self.assertEqual("nb folds = 4, train size ratio = 0.5, "
                         "intents details = [intents_1 -> 5 utterances, "
                         "intents_2 -> 7 utterances]", repr_error)
        self.assertEqual("Not enough data: nb folds = 4, "
                         "train size ratio = 0.5, intents details = "
                         "[intents_1 -> 5 utterances, "
                         "intents_2 -> 7 utterances]", error_message)
