import pdfkit as pdf
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/api/create_document', methods=["GET", "POST"])
def func():
    data = request.json
    if data["Passport"]:
        content = data["Passport"]
        file = pdf.from_string(
            render_template("Passport.html",
                            organization=content.get("organization", "-"),
                            bush_number=content.get("bush_number", "-"),
                            date=content.get("date", ""),
                            team=content.get("team", "-"),
                            name=content.get("name", "-"),
                            fluid_type=content.get("fluid_type", "-"),
                            density=content.get("density", "-"),
                            volume=content.get("volume", "-"),
                            other_works=content.get("other_works", "-"),
                            complect_responsible=content.get("complect_responsible", ""),
                            superior=content.get("superior", ""),
                            start_installation=content.get("start_installation", ""),
                            finish_installation=content.get("finish_installation", ""),
                            temperature=content.get("temperature", ""),
                            precipitation=content.get("precipitation", "без осадков"),
                            uenz=content.get("uenz", ""),
                            well_id=content.get("well_id", ""),
                            customer=content.get("customer", ""),
                            field=content.get("field", ""),
                            cdng_number=content.get("cdng_number", ""),
                            stop_reason=content.get("stop_reason", ""),
                            mrp=content.get("mrp", ""),
                            start_date=content.get("start_date", ""),
                            stop_date=content.get("stop_date", ""),
                            ),
            False,
            css="static/hf.css",
        )

        return file


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=10000)
