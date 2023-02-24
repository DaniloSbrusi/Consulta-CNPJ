from flask import Flask, render_template, request
import basedosdados as bd

app = Flask(__name__)

df = bd.read_table(dataset_id='br_me_cnpj',
                    table_id='socios',
                    billing_project_id='cnpj-377823',
                    limit=100)


@app.route("/teste")
def index():
	return render_template('buscar_socio.html')

@app.route("/find", methods=['POST'])
def find():
    query = request.get_json().strip().upper()
    result = df[df.nome.str.contains(query)]
    return result.to_json(orient='records')

@app.route("/detalhar")
def detalhar():
    dados = df[df.nome.str.contains(request.args.get('nome'))].to_dict(orient='records')
    return render_template('detalhar.html', dados=dados)
    
if __name__ == "__main__":
	app.run(debug=True)
