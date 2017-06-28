from tf.fabric import Fabric
from flask import render_template, request, url_for
from kimsbible import app
from kimsbible.views import api

api.makeAvailableIn(globals())

def sortkeypicker(keynames):
    negate = set()
    for i, k in enumerate(keynames):
        if k[:1] == '-':
            keynames[i] = k[1:]
            negate.add(k[1:])
    def getit(adict):
       composite = [adict[k] for k in keynames]
       for i, (k, v) in enumerate(zip(keynames, composite)):
           if k in negate:
               composite[i] = -v
       return composite
    return getit

def verbaldata(verb):
    verb = verb.replace('ש1', 'שׁ').replace('ש2', 'שׂ')
    query = "word lex_utf8="+verb
    S.search(query)
    fetch_data = list(S.fetch())

    if len(fetch_data) == 0:
        return False

    i = 0
    wordlist = {}
    wholelist = []
    checklist = []
    for w in fetch_data:
        node = w[0]
        if F.ps.v(node) == "unknown":
            ps = ''
        else:
            ps = F.ps.v(node)

        if F.gn.v(node) == "unknown":
            gn = ''
        else:
            gn = F.gn.v(node)

        if F.nu.v(node) == "unknown":
            nu = ''
        else:
            nu = F.nu.v(node)

        if F.prs_ps.v(node) == "unknown":
            prs_ps = ''
        else:
            prs_ps = F.prs_ps.v(node)

        if F.prs_gn.v(node) == "unknown":
            prs_gn = ''
        else:
            prs_gn = F.prs_gn.v(node)

        if F.prs_nu.v(node) == "unknown":
            prs_nu = ''
        else:
            prs_nu = F.prs_nu.v(node)

        checkvalue = F.vs.v(node) + F.vt.v(node) + ps + gn + nu + prs_ps + prs_gn + prs_nu
        if F.pdp.v(node) != "verb" or checkvalue in checklist:
            continue
        else:
            wordlist = {
                "verb":F.g_word_utf8.v(node),
                "stem":F.vs.v(node),
                "tense":F.vt.v(node),
                "ps":ps,
                "gn":gn,
                "nu":nu,
                "prs_ps":prs_ps,
                "prs_gn":prs_gn,
                "prs_nu":prs_nu
            }
            wholelist.append(wordlist)
            checklist.append(F.vs.v(node) + F.vt.v(node) + ps + gn + nu + prs_ps + prs_gn + prs_nu)
            i = i + 1

    if i == 0: return False

    sortedlist = sorted(wholelist, key=sortkeypicker(['stem', 'tense', 'ps', 'gn', 'nu', 'prs_ps', 'prs_gn', 'prs_nu']))

    return sortedlist


@app.route('/conjugator/', methods=['GET', 'POST'])
def conjugator():
    if request.method == 'POST':
        verb = request.form['verb']
        result = verbaldata(verb)
        return render_template('conjugator.html', result=result)
    else:
        return render_template('conjugator.html')
