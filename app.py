from flask import Flask
from views import get_all, get_by_pk, get_by_skill


app = Flask(__name__)


@app.route("/")
def index():
    return get_all()


@app.route("/candidates/<x>")
def page_candidate_profile(x):
    candidate_by_pk = get_by_pk(int(x))
    url = candidate_by_pk['picture']
    return f"<pre><img src='{url}'>\n" \
           f"{candidate_by_pk['name']}\n" \
           f"{candidate_by_pk['position']}\n" \
           f"{candidate_by_pk['skills']}</pre>"


@app.route("/<feed>/")
def page_feed_skill(feed):
    skill_list = ''
    for candidate in get_by_skill(feed):
        skill_list += f"<pre>{candidate['name']}\n" \
                      f"{candidate['position']}\n" \
                      f"{candidate['skills']}</pre>"
    return skill_list


app.run(host='127.0.0.2', port=80)
