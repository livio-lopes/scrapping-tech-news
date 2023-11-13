from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import Mock, patch


def test_reading_plan_group_news():
    instance = ReadingPlanService()
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        instance.group_news_for_available_time(-2)

    mock_value = [
        {"title": "Um bode aventureiro", "reading_time": 4},
        {"title": "Um bode voador", "reading_time": 5},
        {"title": "O bode que roubava livros", "reading_time": 10},
        {"title": "O senhor dos bodes", "reading_time": 12},
    ]
    mock_find_news = Mock(return_value=mock_value)

    expected = {
        "readable": [
            {
                "unfilled_time": 1,
                "chosen_news": [
                    (
                        "Um bode aventureiro",
                        4,
                    ),
                    (
                        "Um bode voador",
                        5,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "O bode que roubava livros",
                        10,
                    )
                ],
            },
        ],
        "unreadable": [
            ("O senhor dos bodes", 12),
        ],
    }
    with patch("tech_news.database.find_news", mock_find_news):
        result = instance.group_news_for_available_time(10)

    assert result == expected
