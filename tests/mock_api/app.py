from threading import Thread
from flask import Flask, request, jsonify, Response

CORRECT_CHALLENGE = "HTB{a_challenge_flag}"
CORRECT_HASH = "30ea86803e0d85be51599c3a4e422266"
CHALLENGE_CRACKTHIS = {"id": 1,
                       "name": "Crack This!",
                       "description": "Crack the program and get the flag!",
                       "category_name": "Reversing",
                       "creator_id": 1,
                       "creator_name": "Nobody",
                       "creator2_id": None,
                       "creator2_name": None,
                       "retired": True,
                       "points": 0,
                       "difficulty_chart": {},
                       "difficulty": "Hard",
                       "solves": 1,
                       "authUserSolve": True,
                       "likes": 1,
                       "dislikes": 1,
                       "release_date": "2017-06-29T19:00:00.000000Z",
                       "docker": False,
                       "docker_ip": None,
                       "download": True
                       }

CHALLENGE_WEATHERAPP = {
    "id": 196,
    "name": "Weather App",
    "retired": False,
    "difficulty": "Easy",
    "points": "30",
    "difficulty_chart": {},
    "solves": 1,
    "authUserSolve": True,
    "likes": 1,
    "dislikes": 1,
    "description": "A pit of eternal darkness, a mindless journey of abeyance, this feels like a never-ending dream. I think I'm hallucinating with the memories of my past life, it's a reflection of how thought I would have turned out if I had tried enough. A weatherman, I said! Someone my community would look up to, someone who is to be respected. I guess this is my way of telling you that I've been waiting for someone to come and save me. This weather application is notorious for trapping the souls of ambitious weathermen like me. Please defeat the evil bruxa that's operating this website and set me free! 🧙‍♀️",
    "category_name": "Web",
    "creator_id": 95,
    "creator_name": "makelarisjr",
    "creator2_id": 107,
    "creator2_name": "makelaris",
    "download": True,
    "docker": True,
    "docker_ip": None,
    "release_date": "2021-01-29T20:00:00.000000Z",
}


CHALLENGE_NGINXATSU = {
    "id": 143,
    "name": "nginxatsu",
    "retired": False,
    "difficulty": "Medium",
    "points": "40",
    "difficulty_chart": {},
    "solves": 1,
    "authUserSolve": True,
    "likes": 1,
    "dislikes": 1,
    "description": "Team Seb managed to abduct nginxatsu from Dr. Talin's hospital after he was submitted there for injuries he sustained from a recent duel. Now they've turned him into a nginx config generator, this is so despicable... YOU HAVE TO SAVE HIM!",
    "category_name": "Web",
    "creator_id": 95,
    "creator_name": "makelarisjr",
    "creator2_id": 107,
    "creator2_name": "makelaris",
    "download": True,
    "docker": True,
    "docker_ip": None,
    "release_date": "2021-01-29T20:00:00.000000Z",
}

CHALLENGE_QUICKR = {
    "id": 119,
    "name": "QuickR",
    "retired": False,
    "difficulty": "Medium",
    "points": "40",
    "difficulty_chart": {},
    "solves": 1,
    "authUserSolve": True,
    "likes": 1,
    "dislikes": 1,
    "description": "Let's see if you're a QuickR soldier as you pretend to be",
    "category_name": "Misc",
    "creator_id": 95,
    "creator_name": "makelarisjr",
    "creator2_id": 107,
    "creator2_name": "makelaris",
    "download": False,
    "docker": True,
    "docker_ip": None,
    "release_date": "2021-01-29T20:00:00.000000Z",
}

USER_CH4P = {
    "id": 1,
    "name": "ch4p",
    "system_owns": 67,
    "user_owns": 67,
    "user_bloods": 0,
    "system_bloods": 0,
    "points": 1,
    "ranking": 1,
    "rank": "Noob",
    "respects": 1,
    "university": None,
    "university_name": None,
    "description": None,
    "github": None,
    "linkedin": None,
    "twitter": None,
    "website": None,
    "current_rank_progress": None,
    "next_rank": None,
    "next_rank_points": None,
    "rank_ownership": 0.0,
    "rank_requirement": None,
    "country_name": None,
    "team": {},
    "public": True
}

USER_MAKELARISJR = {
    "id": 95,
    "name": "makelarisjr",
    "system_owns": 67,
    "user_owns": 67,
    "user_bloods": 0,
    "system_bloods": 0,
    "points": 1,
    "ranking": 1,
    "rank": "Noob",
    "respects": 1,
    "university": None,
    "university_name": None,
    "description": None,
    "github": None,
    "linkedin": None,
    "twitter": None,
    "website": None,
    "current_rank_progress": None,
    "next_rank": None,
    "next_rank_points": None,
    "rank_ownership": 0.0,
    "rank_requirement": None,
    "country_name": None,
    "team": {},
    "public": True
}

USER_MAKELARIS = {
    "id": 107,
    "name": "makelaris",
    "system_owns": 67,
    "user_owns": 67,
    "user_bloods": 0,
    "system_bloods": 0,
    "points": 1,
    "ranking": 1,
    "rank": "Noob",
    "respects": 1,
    "university": None,
    "university_name": None,
    "description": None,
    "github": None,
    "linkedin": None,
    "twitter": None,
    "website": None,
    "current_rank_progress": None,
    "next_rank": None,
    "next_rank_points": None,
    "rank_ownership": 0.0,
    "rank_requirement": None,
    "country_name": None,
    "team": {},
    "public": True
}

USER_HTBBOT = {
    "id": 16,
    "name": "HTB Bot",
    "system_owns": 67,
    "user_owns": 67,
    "user_bloods": 0,
    "system_bloods": 0,
    "points": 1,
    "ranking": 1,
    "rank": "Noob",
    "respects": 1,
    "university": None,
    "university_name": None,
    "description": None,
    "github": None,
    "linkedin": None,
    "twitter": None,
    "website": None,
    "current_rank_progress": None,
    "next_rank": None,
    "next_rank_points": None,
    "rank_ownership": 0.0,
    "rank_requirement": None,
    "country_name": None,
    "team": {},
    "public": True
}

USER_ISTARCHEATERS = {
    "id": 272569,
    "name": "IStarCheaters",
    "system_owns": 67,
    "user_owns": 67,
    "user_bloods": 0,
    "system_bloods": 0,
    "points": 1,
    "ranking": 1,
    "rank": "Noob",
    "respects": 1,
    "university": None,
    "university_name": None,
    "description": None,
    "github": None,
    "linkedin": None,
    "twitter": None,
    "website": None,
    "current_rank_progress": None,
    "next_rank": None,
    "next_rank_points": None,
    "rank_ownership": 0.0,
    "rank_requirement": None,
    "country_name": None,
    "team": None,
    "public": True
}

USER_CLUBBY = {
    "id": 83743,
    "name": "clubby789",
    "server_id": 254,
    "avatar": None,
    "beta_tester": 0,
    "rank_id": 7,
    "onboarding_completed": True,
    "verified": True,
    "can_delete_avatar": True,
    "team": {
      "id": 1709,
      "name": "WinBARs",
    },
    "university": None,
    "hasTeamInvitation": True,
    "subscription_plan": None,
    "user_owns": 1,
    "system_owns": 1,
    "root_owns": 1,
    "user_bloods": 1,
    "system_bloods": 1,
    "root_bloods": 1,
    "points": 1,
    "ranking": 1,
    "rank": "Noob",
    "respects": 1,
    "university_name": None,
    "description": None,
    "github": None,
    "linkedin": None,
    "twitter": None,
    "website": None,
    "current_rank_progress": None,
    "next_rank": None,
    "next_rank_points": None,
    "rank_ownership": 0.0,
    "rank_requirement": None,
    "country_name": None,
    "public": True
}


USER_EKS = {
    "id": 302,
    "name": "eks",
    "avatar": None,
    "beta_tester": 0,
    "rank_id": 7,
    "onboarding_completed": True,
    "verified": True,
    "can_delete_avatar": True,
    "team": None,
    "university": None,
    "hasTeamInvitation": True,
    "subscription_plan": None,
    "user_owns": 1,
    "system_owns": 1,
    "user_bloods": 1,
    "system_bloods": 1,
    "points": 1,
    "ranking": 1,
    "rank": "Noob",
    "respects": 1,
    "university_name": None,
    "description": None,
    "github": None,
    "linkedin": None,
    "twitter": None,
    "website": None,
    "current_rank_progress": None,
    "next_rank": None,
    "next_rank_points": None,
    "rank_ownership": 0.0,
    "rank_requirement": None,
    "country_name": None,
    "public": True
}

MACHINE_LAME = {
    "id": 1,
    "name": "Lame",
    "os": "Linux",
    "active": 1,
    "retired": 1,
    "ip": "10.10.10.3",
    "points": 0,
    "static_points": 20,
    "release": "2017-03-14T19:54:51.000000Z",
    "user_owns_count": 1,
    "root_owns_count": 1,
    "free": False,
    "authUserInUserOwns": True,
    "authUserInRootOwns": True,
    "authUserHasReviewed": False,
    "stars": "4.4",
    "difficulty": 26,
    "feedbackForChart": {},
    "difficultyText": "Easy",
    "isCompleted": True,
    "last_reset_time": None,
    "playInfo": {
      "isSpawned": None,
      "isSpawning": None,
      "isActive": False,
      "active_player_count": None,
      "expires_at": None
    },
    "maker": {
      "id": 1,
      "name": "ch4p",
    },
    "maker2": None,
    "userBlood": {},
    "rootBlood": {},
    "recommended": 0,
    "sp_flag": 0,
    "avatar": None,
    "authUserFirstUserTime": "2Y 5M 17D",
    "authUserFirstRootTime": "2Y 5M 17D",
}

ENDGAME_POO = {
    "id": 1,
    "name": "P.O.O.",
    "avatar_url": None,
    "cover_image_url": None,
    "retired": True,
    "vip": True,
    "creators": [
      {
        "id": 302,
        "name": "eks",
      }
    ],
    "points": 0,
    "players_completed": 944,
    "endgame_reset_votes": 0,
    "most_recent_reset": None,
    "entry_points": [],
    "video_url": None,
    "description": None,
    "completion_icon": "fa-chess",
    "completion_text": "Castling",
    "has_user_finished": True
  }

FORTRESS_JET = {
    "id": 1,
    "name": "Jet",
    "image": "",
    "cover_image_url": "",
    "new": False,
    "number_of_flags": 11,
    "user_availability": {
        "available": False,
        "code": 0,
        "message": None
    },
    "flags": [],
    "company": {
        "id": 1,
        "name": None,
        "description": None,
        "url": None,
        "image": None
    },
    "reset_votes": 0,
    "progress_percent": 0,
    "ip": None
}

TEAM_WINRARS = {
    "id": 2710,
    "name": "TheWINRaRs",
    "points": 11,
    "motto": None,
    "description": None,
    "country_name": "United Kingdom",
    "country_code": "GB",
    "cover_image_url": None,
    "twitter": None,
    "facebook": None,
    "discord": None,
    "public": True,
    "avatar_url": None,
    "can_delete_avatar": False,
    "captain": {
        "id": 293491,
        "name": "lukevaxhacker",
    },
    "is_respected": False,
    "join_request_sent": False
}

TEAM_ADMINS = {
    "id": 2710,
    "name": "TheWINRaRs",
    "points": 11,
    "motto": None,
    "description": "",
    "country_name": "Greece",
    "country_code": "GB",
    "cover_image_url": None,
    "twitter": None,
    "facebook": None,
    "discord": None,
    "public": True,
    "avatar_url": None,
    "can_delete_avatar": False,
    "captain": {
        "id": 1,
        "name": "ch4p",
    },
    "is_respected": False,
    "join_request_sent": False
}


has_ratelimited: bool = False

app = Flask(__name__)


@app.route("/api/v4/challenge/list", methods=["GET"])
def list_challenges():
    return jsonify({"challenges": [CHALLENGE_CRACKTHIS for _ in range(30)]})


@app.route("/api/v4/challenge/list/retired", methods=["GET"])
def list_retired_challenges():
    return jsonify({"challenges": [CHALLENGE_CRACKTHIS for _ in range(30)]})


@app.route("/api/v4/challenge/info/<num>", methods=["GET"])
def get_challenge(num):
    num = int(num)
    if num == 1:
        return jsonify({"challenge": CHALLENGE_CRACKTHIS})
    if num == 143:
        return jsonify({"challenge": CHALLENGE_NGINXATSU})
    if num == 119:
        return jsonify({"challenge": CHALLENGE_QUICKR})
    if num == 196:
        return jsonify({"challenge": CHALLENGE_WEATHERAPP})
    return jsonify({"message": "Challenge not found"}), 404


@app.route("/api/v4/challenge/own", methods=["POST"])
def own_challenge():
    if request.json['flag'] == CORRECT_CHALLENGE:
        return jsonify({"message": "Congratulations"})
    else:
        return jsonify({"message": "Incorrect flag"})


@app.route("/api/v4/machine/list")
def list_machines():
    return jsonify({"info": [MACHINE_LAME for _ in range(20)]})


@app.route("/api/v4/machine/list/retired")
def list_retired_machines():
    return jsonify({"info": [MACHINE_LAME for _ in range(150)]})


@app.route("/api/v4/machine/own", methods=["POST"])
def own_machine():
    if request.json['flag'] == CORRECT_HASH:
        return jsonify({"message": "Congratulations"})
    else:
        return jsonify({"message": "Incorrect flag!"})


@app.route("/api/v4/machine/profile/<num>")
def get_machine(num):
    num = int(num)
    if num == 1:
        return jsonify({"info": MACHINE_LAME})


@app.route("/api/v4/login", methods=["POST"])
def login():
    return jsonify({"message": {
        "access_token": "FakeToken",
        "refresh_token": "FakeToken",
        "is2FAEnabled": False
    }})


@app.route("/api/v4/challenge/start", methods=["POST"])
def start_challenge():
    if request.json['challenge_id'] == 143:
        return jsonify({"message": "Instance Created!", "id": "webnginxatsu-83743",
                        "port": 31475, "ip": "10.10.10.10"})
    else:
        return jsonify({"message": "Incorrect Parameters"})


@app.route("/api/v4/challenge/stop", methods=["POST"])
def stop_challenge():
    return jsonify({"message": "Container Stopped"})


@app.route("/api/v4/endgame/<_num>/flag", methods=["POST"])
def submit_endgame_flag(_num):
    if request.json['flag'] == CORRECT_HASH:
        return jsonify({"message": "Congratulations"})
    else:
        return jsonify({"message": "Wrong flag"})


@app.route("/api/v4/endgames")
def get_endgames():
    return jsonify({"data": [ENDGAME_POO for _ in range(5)]})


@app.route("/api/v4/endgame/<num>")
def get_endgame(num):
    num = int(num)
    if num == 1:
        return jsonify({"data": ENDGAME_POO})
    return jsonify({"message": "No results for this endgame"}), 404


@app.route("/api/v4/fortresses")
def list_fortresses():
    return jsonify({"data": {str(i): FORTRESS_JET for i in range(3)}})


@app.route("/api/v4/fortress/<num>")
def get_fortress(num):
    num = int(num)
    if num == 1:
        return jsonify({"data": FORTRESS_JET})


@app.route("/api/v4/fortress/<_num>/flag", methods=["POST"])
def submit_fortress_flag(_num):
    if request.json['flag'] == CORRECT_HASH:
        return jsonify({"message": "Congratulations"})
    else:
        return jsonify({"message": "Wrong flag"})


@app.route("/api/v4/challenge/download/<_num>")
def download_challenge(_num):
    return Response(b"Not really zip data", mimetype="application/zip")


@app.route("/api/v4/rankings/users")
def get_user_list():
    return jsonify({"data": [USER_CLUBBY for _ in range(100)]})


@app.route("/api/v4/rankings/teams")
def get_team_list():
    return jsonify({"data": [{"id": 100, "name": "schmangs"} for _ in range(100)]})


@app.route("/api/v4/rankings/countries")
def get_country_list():
    c = {
        "id": 1, "country": "UK", "name": "United Kingdom",
        "rank": 1, "points": 1, "members": 1,
        "user_owns": 1, "root_owns": 1, "challenge_owns": 1,
        "user_bloods": 1, "root_bloods": 1, "challenge_bloods": 1,
        "fortress": 1, "endgame": 1

    }
    return jsonify({"data": [c for _ in range(100)]})


@app.route("/api/v4/rankings/universities")
def get_uni_list():
    u = {
        "id": 1, "name": "Uni Uni",
        "rank": 1, "points": 1, "students": 1,
        "user_owns": 1, "root_owns": 1, "challenge_owns": 1,
        "user_bloods": 1, "root_bloods": 1, "challenge_bloods": 1,
        "fortress": 1, "endgame": 1

    }
    return jsonify({"data": [u for _ in range(100)]})


@app.route("/api/v4/team/info/<tid>")
def get_team(tid):
    tid = int(tid)
    if tid == 21:
        return jsonify(TEAM_ADMINS)
    if tid == 2710:
        return jsonify(TEAM_WINRARS)
    return jsonify({"message": "No results for this team"}), 404


@app.route("/api/v4/team/stats/owns/<_tid>")
def get_team_owns(_tid):
    return jsonify({"rank": 1})


@app.route("/api/v4/user/profile/basic/<uid>")
def get_basic_profile(uid):
    uid = int(uid)
    if uid == 1:
        return jsonify({"profile": USER_CH4P})
    if uid == 16:
        return jsonify({"profile": USER_HTBBOT})
    if uid == 95:
        return jsonify({"profile": USER_MAKELARISJR})
    if uid == 107:
        return jsonify({"profile": USER_MAKELARIS})
    if uid == 302:
        return jsonify({"profile": USER_EKS})
    if uid == 272569:
        return jsonify({"profile": USER_ISTARCHEATERS})
    if uid == 83743:
        return jsonify({"profile": USER_CLUBBY})
    return jsonify({"message": "No results for this user"}), 404


@app.route("/api/v4/user/profile/activity/<_uid>")
def get_user_activity(_uid):
    return jsonify({"profile": {"activity": []}})


@app.route("/api/v4/user/info")
def get_own_user():
    return jsonify({"info": USER_CLUBBY})


@app.route("/api/v4/search/fetch")
def search():
    return jsonify({"challenges": [], "machines": [MACHINE_LAME], "teams": [], "users": []})


def start_server(port: int):
    thread = Thread(target=app.run, args=('0.0.0.0', port), daemon=True)
    thread.start()