import os
import pickle
import pandas as pd
from flask import Flask, request, Response
from HealthInsurance import HealthInsurance

#loading data
model = pickle.load( open( 'model_logistic_regression.pkl', 'rb' ) )

#initiaalize API
app=Flask( __name__ )

@app.route( '/predict', methods=['POST'] )
def health_insurance_predict():
    
    test_json = request.get_json()

    if test_json:
        
        if isinstance( test_json, dict ):
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else:
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        #initialize health class
        pipeline = HealthInsurance()
        print('\n\n\n')
        print(test_raw.columns.to_list())
        #data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        print('\n\n\n')
        print(test_raw.columns.to_list())
        #feature engineering
        df2 = pipeline.feature_engineering( df1 )
        print('\n\n\n')
        print(test_raw.columns.to_list())
        #data preparation
        df3 = pipeline.data_preparation( df2 )
        print('\n\n\n')
        print(test_raw.columns.to_list())
        print('\n')
        print(df3.shape)       
        print(df3.isna().sum())
        #prediction
        df_response = pipeline.get_prediction( model, df3, test_raw )
        print('\n\n\n')
        print(test_raw.columns.to_list())
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json' )
    
if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 ) 
    app.run( host='0.0.0.0', port=port )
