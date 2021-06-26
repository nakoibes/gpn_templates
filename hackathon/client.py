import requests

# requests.post('http://localhost:5000/api/create_document', json={"mytext": {"the_title": "kek"}})
res = requests.post('http://localhost:5000/api/create_document',
                    json={
                        "PreparationWell":
                            {
                                "bush_number": "100 крайний",
                                "date": "17 марта 2020",
                                "organization": "Квасочек",
                                "team": "13",
                                "name": "Башмачкин Иван Ильич",
                                "volume": "1000",
                                "start_installation": "12:00 18.03",
                                "finish_installation": "16:00 18.03.2020",
                                "temperature": "-13"
                            }})
if res.ok:
    with open('response.pdf', 'wb') as f:
        f.write(res.content)
    # res.decode("base64")
    # pdf.from_string(render_template("Passport.html", the_title=title), "example.pdf", css="static/hf.css")
    # print(res.json())
