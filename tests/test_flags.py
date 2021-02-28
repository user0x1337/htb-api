from pytest import raises
from hackthebox import HTBClient, Machine, Challenge, Endgame
from hackthebox.errors import IncorrectFlagException, IncorrectArgumentException


CORRECT_CHALLENGE = "HTB{a_challenge_flag}"
CORRECT_HASH = "30ea86803e0d85be51599c3a4e422266"


def test_machine_flags(mock_htb_client: HTBClient):
    """Tests the ability to submit machine flags"""
    # Create a fake machine to test with
    machine = Machine({
        "id": 1,
        "name": "Lame",
        "os": "Linux",
        "points": 0,
        "release": "2021-02-27T17:00:00.000000Z",
        "user_owns_count": 0,
        "root_owns_count": 0,
        "authUserInUserOwns": False,
        "authUserInRootOwns": False,
        "authUserHasReviewed": False,
        "stars": 0.0,
        "avatar": "nothing.png",
        "difficultyText": "Easy",
        "free": False,
        "maker": {
            "id": 1
        },
        "maker2": None
    }, mock_htb_client, summary=True)
    assert machine.submit(CORRECT_HASH, 10) is True

    with raises(IncorrectFlagException):
        machine.submit("wrong", 10)

    with raises(IncorrectArgumentException):
        machine.submit(CORRECT_HASH, 5)


def test_challenge_flags(mock_htb_client: HTBClient):
    """Tests the ability to submit challenge flags"""
    # Create a fake challenge to test with
    challenge = Challenge({
        "id": 1,
        "name": "Crack This",
        "retired": True,
        "points": 0,
        "difficulty_chart": "0",
        "release_date": "2018-04-25",
        "solves": 0,
        "authUserSolve": False,
        "likes": False,
        "dislikes": False
    }, mock_htb_client, summary=True)
    assert challenge.submit(CORRECT_CHALLENGE, 10) is True

    with raises(IncorrectFlagException):
        challenge.submit("wrong", 10)

    with raises(IncorrectArgumentException):
        challenge.submit(CORRECT_CHALLENGE, 5)


def test_endgame_flags(mock_htb_client: HTBClient):
    """Tests the ability to submit endgame flags"""
    # Create a fake endgame to test with
    endgame = Endgame({
        "id": 1,
        "name": "P.O.O.",
        "avatar_url": "nothing.png",
        "cover_image_url": "nothing.png",
        "retired": True,
        "vip": True,
        "creators": [{
            "id": 302,
            "name": "eks",
            }, {
            "id": 2984,
            "name": "mrb3n",
            }]
    }, mock_htb_client, summary=True)
    assert endgame.submit(CORRECT_HASH) is True

    with raises(IncorrectFlagException):
        endgame.submit("wrong")
