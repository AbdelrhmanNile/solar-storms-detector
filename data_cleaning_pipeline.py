import pandas as pd

def crop_dataset(df):
    cols = ["Ang_dev", "BX","BY","BZ","ChisQ_DOF_nonlin","EW_flowangle","NS_flowangle","Proton_Np_moment","Proton_Np_nonlin","Proton_VX_moment","Proton_VX_nonlin","Proton_VY_moment","Proton_VY_nonlin","Proton_VZ_moment","Proton_VZ_nonlin","Proton_V_moment","Proton_V_nonlin","Proton_W_moment","Proton_W_nonlin","Proton_Wpar_moment","Proton_Wpar_nonlin","Proton_Wperp_moment","Proton_Wperp_nonlin","Proton_sigmaNp_nonlin","Proton_sigmaVX_nonlin","Proton_sigmaVY_nonlin","Proton_sigmaVZ_nonlin","Proton_sigmaV_nonlin","Proton_sigmaW_nonlin","Proton_sigmaWpar_nonlin","Proton_sigmaWperp_nonlin","dev","xgse","ygse","ygsm","zgse","zgsm"]
    df = df[cols]
    return df

def remove_spikes(df):
    df.drop(df[df['Proton_Np_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_Np_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_VX_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_VX_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_VY_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_VY_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_VZ_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_VZ_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_V_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_V_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_W_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_W_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_Wpar_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_Wpar_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_Wperp_moment'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_Wperp_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaNp_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaVX_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaVY_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaVZ_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaV_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaW_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaWpar_nonlin'] >= 99998].index, inplace = True)
    df.drop(df[df['Proton_sigmaWperp_nonlin'] >= 99998].index, inplace = True)
    
    ##
    df.drop(df[df['Proton_Np_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_Np_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_VX_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_VX_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_VY_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_VY_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_VZ_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_VZ_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_V_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_V_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_W_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_W_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_Wpar_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_Wpar_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_Wperp_moment'] == 1].index, inplace = True)
    df.drop(df[df['Proton_Wperp_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaNp_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaVX_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaVY_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaVZ_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaV_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaW_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaWpar_nonlin'] == 1].index, inplace = True)
    df.drop(df[df['Proton_sigmaWperp_nonlin'] == 1].index, inplace = True)
    ##
    df.drop(df[df['Proton_Np_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_Np_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_VX_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_VX_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_VY_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_VY_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_VZ_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_VZ_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_V_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_V_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_W_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_W_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_Wpar_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_Wpar_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_Wperp_moment'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_Wperp_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaNp_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaVX_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaVY_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaVZ_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaV_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaW_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaWpar_nonlin'] == 10000].index, inplace = True)
    df.drop(df[df['Proton_sigmaWperp_nonlin'] == 10000].index, inplace = True)
    
    return df
    
def data_cleaning(df_path):
    df = pd.read_csv(df_path)
    cleaned_df = crop_dataset(df)
    final_df = remove_spikes(cleaned_df)
    final_df.to_csv('cleaned_norm_test.csv', index = False)


data_cleaning('norm_test.csv')