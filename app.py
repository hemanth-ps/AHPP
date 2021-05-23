import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    x = [i for i in request.form.values()]
    if x[1]=='RL':
        x[1]=3
    elif x[1]=='RM':
        x[1]=1
    elif x[1]=='FV':
        x[1]=4
    elif x[1]=='RH':
        x[1]=2
    else:
        x[1]=0 

    if x[2]=='NAmes':
        x[2]=8 
    elif x[2]=='CollgCr':
        x[2]=14
    elif x[2]=='OldTown':
        x[2]=4
    elif x[2]=='Edwards':
        x[2]=5
    elif x[2]=='Somerst':
        x[2]=18
    elif x[2]=='Gilbert':
        x[2]=13
    elif x[2]=='NridgHt':
        x[2]=21
    elif x[2]=='Sawyer':
        x[2]=6
    elif x[2]=='NWAmes':
        x[2]=12
    elif x[2]=='SawyerW':
        x[2]=10
    elif x[2]=='BrkSide':
        x[2]=3
    elif x[2]=='Crawfor':
        x[2]=16
    elif x[2]=='Mitchel':
        x[2]=9
    elif x[2]=='NoRidge':
        x[2]=22
    elif x[2]=='Timber':
        x[2]=19
    elif x[2]=='IDOTRR':
        x[2]=0
    elif x[2]=='ClearCr':
        x[2]=17
    elif x[2]=='StoneBr':
        x[2]=20
    elif x[2]=='SWISU':
        x[2]=7
    elif x[2]=='MeadowV':
        x[2]=1
    elif x[2]=='Blmngtn':
        x[2]=15
    elif x[2]=='BrDale':
        x[2]=2
    else:
        x[2]=11

    if x[5]=='Gable':
        x[5]=0
    elif x[5]=='Hip':
        x[5]=2
    else:
        x[5]=1
    
    if x[6]=='TA':
        x[6]=2
    elif x[6]=='Gd':
        x[6]=3
    elif x[6]=='Ex':
        x[6]=4
    elif x[6]=='Fa':
        x[6]=1
    else:
        x[6]=0

    if x[7]=='No':
        x[7]=1
    elif x[7]=='Av':
        x[7]=3
    elif x[7]=='Gd':
        x[7]=4
    elif x[7]=='Mn':
        x[7]=2
    else:
        x[7]=0    

    if x[8]=='Ex':
        x[8]=4
    elif x[8]=='Gd':
        x[8]=3
    elif x[8]=='Fa':
        x[8]=1
    elif x[8]=='Po':
        x[8]=0
    elif x[8]=='TA':
        x[8]=2

    if x[9]=='Y':
        x[9]=1
    elif x[9]=='N':
        x[9]=0

    if x[13]=='Ex':
        x[13]=3
    elif x[13]=='Gd':
        x[13]=2
    elif x[13]=='Fa':
        x[13]=0
    elif x[13]=='TA':
        x[13]=1


    if x[15]=='Ex':
        x[15]=5
    elif x[15]=='Gd':
        x[15]=4
    elif x[15]=='Fa':
        x[15]=2
    elif x[15]=='Po':
        x[15]=0
    elif x[15]=='TA':
        x[15]=3
    else:
        x[15]=1

    if x[16]=='Attchd':
        x[16]=4
    elif x[16]=='Detchd':
        x[16]=2
    elif x[16]=='BuiltIn':
        x[16]=5
    elif x[16]=='Basment':
        x[16]=3
    elif x[16]=='CarPort':
        x[16]=1
    elif x[16]=='2Types':
        x[16]=1
    else:
        x[16]=0

    if x[17]=='RFn':
        x[17]=2
    elif x[17]=='Unf':
        x[17]=1
    elif x[17]=='Fin':
        x[17]=3
    else:
        x[17]=0

    if x[19]=='Y':
        x[19]=2
    elif x[19]=='N':
        x[19]=0
    elif x[19]=='P':
        x[19]=1

    if x[20]=='Abnorml':
        x[20]=0
    elif x[20]=='Rare':
        x[20]=1
    elif x[20]=='Family':
        x[20]=2
    elif x[20]=='Normal':
        x[20]=3
    elif x[20]=='Partial':
        x[20]=4

    x = np.array(x).reshape(-1,1)
    final_list = []
    for i in x:
        for h in i:
            final_list.append(h)
    final_list = np.array(final_list)
    final_list = final_list.reshape(1,-1)
    prediction = model.predict(final_list)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='House Price will be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values())).reshape(1,-1)])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)