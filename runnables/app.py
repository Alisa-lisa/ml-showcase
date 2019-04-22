from flask import Flask, request, jsonify
from nn_generator.config_parser import config_parser
from nn_generator.model_generator.simple_nn import SimpleNN, read_out_model
from utils import extract_features
import numpy as np

app = Flask("ml-service-proto")

# prepare model
config = config_parser.read_out_config("models/myconfig.json")
nn = SimpleNN(config)
print(type(nn))
model, meta = read_out_model("models/mymodel.json")

def human_predict(timestamp, model, meta):
    """ helper function to predict the state based on the timestamp """
    now_extracted = extract_features(float(timestamp), 4)
    depth = meta["architecture"]["depth"]
    predicted = nn.predict(np.array([now_extracted]).T, model, depth, True)
    return "Awake" if int(predicted[0][0]) == 1 else "Sleeping"


@app.route('/predict')
def predict():
    """
    Simple predict function: get data from request, extract features, predict
    :return: prediction
    """
    # get data in
    timestamp = None
    try:
        timestamp = request.args.get('input')
    except:
        pass
    # prepare features
    if timestamp is not None:
        prepared_input = extract_features(timestamp)
        return jsonify({"Message":"Input missing",
                        "Result": human_predict(timestamp, model, meta)})
    else:
        return jsonify({"Message":"Input missing", "Result":-1.0})




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)