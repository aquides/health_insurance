import pandas as pd
import numpy as np
from inflection import underscore
import pickle

class HealthInsurance( object ):
    def __init__( self ):
        self.annual_premium_scaler             = pickle.load( open(  'annual_premium_scaler.pkl', 'rb' ) )
        self.age_scaler                        = pickle.load( open(  'age_scaler.pkl', 'rb' ) )
        self.vintage_scaler                    = pickle.load( open(  'vintage_scaler.pkl', 'rb' ) )
        self.target_encode_gender_scaler       = pickle.load( open(  'target_encode_gender_scaler.pkl', 'rb' ) )
        self.target_encode_region_code_scaler  = pickle.load( open(  'target_encode_region_code_scaler.pkl', 'rb' ) )
        self.fe_policy_sales_channel_scaler    = pickle.load( open(  'fe_policy_sales_channel_scaler.pkl', 'rb' ) )
    
    def data_cleaning( self, df1 ):
        df1.columns = [underscore(k) for k in df1.columns.tolist()]
        
        return df1
    
    def feature_engineering( self, df2 ):

        #vehicle damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply( lambda x: 1 if x == 'Yes' else 0)
        
        return df2
        
    def data_preparation(self, df3):
        #annual premium
        df3['annual_premium'] = self.annual_premium_scaler.transform( df3[['annual_premium']].values )
        #5.2 RESCALING
        #reescalar os intervalos entre 0 e 1

        #age
        df3['age'] = self.age_scaler.transform( df3[['age']].values)

        #vintage
        df3['vintage'] = self.vintage_scaler.transform( df3[['vintage']].values)
        #5.3 ENCODER
        #gender
        df3.loc[:, 'gender'] = df3['gender'].map( self.target_encode_gender_scaler )

        #region code - target encond/ferquency/weighted #muitos valores para hot
        # usa media da frequencia dos outros valores [ara atribui-los valores]
        df3.loc[:, 'region_code'] = df3['region_code'].map( self.target_encode_region_code_scaler )

        # vehicle age - One Hot / Order enconding/Frequency
        #df3 = pd.get_dummies(df3, prefix='vehicle_age', columns=['vehicle_age'])
        #dummies transforma cat em onr hot. Pessimo quando se tem muitos valores diferrente spois deixa gigante o DF

        #policy sales channel - Frequency Encoding/ target
        df3.loc[:, 'policy_sales_channel'] = df3['policy_sales_channel'].map( self.fe_policy_sales_channel_scaler )
       
        #Features selection
        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 'vehicle_damage', 'previously_insured', 'policy_sales_channel']

        return df3[ cols_selected ]
    
    def get_prediction(self, model, prepared_dataset, original_dataset):
        yhat = model.predict_proba(prepared_dataset)
        original_dataset['response'] = yhat
        
        return original_dataset.to_json(orient="records")
