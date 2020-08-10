# imports
import pandas as pd
from time import time

myPath = 'c:\\Users\\Liron\\Desktop\\Projects\\Soccer Games Prediction\\'


data = pd.read_csv(myPath + 'projectdata.csv')
df_Teams = pd.read_csv(myPath + 'df_Teams.csv')
df_Referee = pd.read_csv(myPath + 'df_Referee.csv')


# Functions
def getMyData(filePath):
    df = pd.read_csv(filePath)
    df = df.dropna()  # For later use in case of bad row
    df = df.reset_index(drop=True)
    len(df)
    return df


def addTeam(team):
    global df_Teams

    df_Teams = df_Teams.append({"team": team
                                   , "H_Games": 0, "H_FTWins": 0, "H_FTDraws": 0, "H_FTLost": 0, "H_HTWins": 0,
                                "H_HTDraws": 0, "H_HTLost": 0, "H_FTGF": 0, "H_FTGA": 0, "H_FTGD": 0, "H_HTGF": 0
                                   , "H_HTGA": 0, "H_HTGD": 0, "H_SF": 0, "H_SA": 0, "H_SoTF": 0, "H_SoTA": 0,
                                "H_CF": 0, 'H_CA': 0, "H_FF": 0, "H_FA": 0, "H_YCF": 0, "H_YCA": 0, "H_RCF": 0,
                                "H_RCA": 0
                                   , "A_Games": 0, "A_FTWins": 0, "A_FTDraws": 0, "A_FTLost": 0, "A_HTWins": 0,
                                "A_HTDraws": 0, "A_HTLost": 0, "A_FTGF": 0, "A_FTGA": 0, "A_FTGD": 0, "A_HTGF": 0
                                   , "A_HTGA": 0, "A_HTGD": 0, "A_SF": 0, "A_SA": 0, "A_SoTF": 0, "A_SoTA": 0,
                                "A_CF": 0, 'A_CA': 0, "A_FF": 0, "A_FA": 0, "A_YCF": 0, "A_YCA": 0, "A_RCF": 0,
                                "A_RCA": 0
                                }, ignore_index=True)


def addRef(ref):
    global df_Referee

    df_Referee = df_Referee.append({"Name": ref, "Games": 0, "YD": 0, "RD": 0, "FKC": 0, "YPG": 0, "RPG": 0, "FKCPG": 0
                                    }, ignore_index=True)


def updateTeamsTable(Side, OtherSide, row, team):
    global df_Teams

    FTHG = row['FT' + Side + 'G']
    FTAG = row['FT' + OtherSide + 'G']
    FTR = row['FTR']
    HTHG = row['HT' + Side + 'G']
    HTAG = row['HT' + OtherSide + 'G']
    HTR = row['HTR']
    HS = row[Side + 'S']
    AS = row[OtherSide + 'S']
    HST = row[Side + 'ST']
    AST = row[OtherSide + 'ST']
    HF = row[Side + 'F']
    AF = row[OtherSide + 'F']
    HC = row[Side + 'C']
    AC = row[OtherSide + 'C']
    HY = row[Side + 'Y']
    AY = row[OtherSide + 'Y']
    HR = row[Side + 'R']
    AR = row[OtherSide + 'R']

    df_Teams.loc[df_Teams['team'] == team, [Side + '_Games']] = \
        df_Teams[df_Teams['team'] == team][Side + '_Games'].values[0] + 1
    if FTR == Side:
        df_Teams.loc[df_Teams['team'] == team, [Side + '_FTWins']] = \
            df_Teams[df_Teams['team'] == team][Side + '_FTWins'].values[0] + 1  # Full Time Wins
    elif FTR == 'D':
        df_Teams.loc[df_Teams['team'] == team, [Side + '_FTDraws']] = \
            df_Teams[df_Teams['team'] == team][Side + '_FTDraws'].values[0] + 1  # Full Time Draws
    else:
        df_Teams.loc[df_Teams['team'] == team, [Side + '_FTLost']] = \
            df_Teams[df_Teams['team'] == team][Side + '_FTLost'].values[0] + 1  # Full Time Lost
    if HTR == Side:
        df_Teams.loc[df_Teams['team'] == team, [Side + '_HTWins']] = \
            df_Teams[df_Teams['team'] == team][Side + '_HTWins'].values[0] + 1  # Half Time Wins
    elif HTR == 'D':
        df_Teams.loc[df_Teams['team'] == team, [Side + '_HTDraws']] = \
            df_Teams[df_Teams['team'] == team][Side + '_HTDraws'].values[0] + 1  # Half Time Draws
    else:
        df_Teams.loc[df_Teams['team'] == team, [Side + '_HTLost']] = \
            df_Teams[df_Teams['team'] == team][Side + '_HTLost'].values[0] + 1  # Half Time Lost
    df_Teams.loc[df_Teams['team'] == team, [Side + '_FTGF']] = \
        df_Teams[df_Teams['team'] == team][Side + '_FTGF'].values[0] + FTHG  # Full Time Goals For
    df_Teams.loc[df_Teams['team'] == team, [Side + '_FTGA']] = \
        df_Teams[df_Teams['team'] == team][Side + '_FTGA'].values[0] + FTAG  # Full Time Goals Agienst
    df_Teams.loc[df_Teams['team'] == team, [Side + '_FTGD']] = \
        df_Teams[df_Teams['team'] == team][Side + '_FTGF'].values[0] - \
        df_Teams[df_Teams['team'] == team][Side + '_FTGA'].values[0]  # Full Time Goal Diffence
    df_Teams.loc[df_Teams['team'] == team, [Side + '_HTGF']] = \
        df_Teams[df_Teams['team'] == team][Side + '_HTGF'].values[0] + HTHG  # Half Time Goals For
    df_Teams.loc[df_Teams['team'] == team, [Side + '_HTGA']] = \
        df_Teams[df_Teams['team'] == team][Side + '_HTGA'].values[0] + HTAG  # Half Time Goals Agienst
    df_Teams.loc[df_Teams['team'] == team, [Side + '_HTGD']] = \
        df_Teams[df_Teams['team'] == team][Side + '_HTGF'].values[0] - \
        df_Teams[df_Teams['team'] == team][Side + '_HTGA'].values[0]  # Half Time Goal Diffence
    df_Teams.loc[df_Teams['team'] == team, [Side + '_SF']] = df_Teams[df_Teams['team'] == team][Side + '_SF'].values[
                                                                 0] + HS  # Shots For
    df_Teams.loc[df_Teams['team'] == team, [Side + '_SA']] = df_Teams[df_Teams['team'] == team][Side + '_SA'].values[
                                                                 0] + AS  # Shots Agienst
    df_Teams.loc[df_Teams['team'] == team, [Side + '_SoTF']] = \
        df_Teams[df_Teams['team'] == team][Side + '_SoTF'].values[0] + HST  # Shots on Target For
    df_Teams.loc[df_Teams['team'] == team, [Side + '_SoTA']] = \
        df_Teams[df_Teams['team'] == team][Side + '_SoTA'].values[0] + AST  # Shots on Target Agienst
    df_Teams.loc[df_Teams['team'] == team, [Side + '_CF']] = df_Teams[df_Teams['team'] == team][Side + '_CF'].values[
                                                                 0] + HC  # Corners For
    df_Teams.loc[df_Teams['team'] == team, [Side + '_CA']] = df_Teams[df_Teams['team'] == team][Side + '_CA'].values[
                                                                 0] + AC  # Corners Agienst
    df_Teams.loc[df_Teams['team'] == team, [Side + '_FF']] = df_Teams[df_Teams['team'] == team][Side + '_FF'].values[
                                                                 0] + HF  # Fouls Committed by rival
    df_Teams.loc[df_Teams['team'] == team, [Side + '_FA']] = df_Teams[df_Teams['team'] == team][Side + '_FA'].values[
                                                                 0] + AF  # Fouls Committed by the team
    df_Teams.loc[df_Teams['team'] == team, [Side + '_YCF']] = df_Teams[df_Teams['team'] == team][Side + '_YCF'].values[
                                                                  0] + HY  # Yellow Cards For
    df_Teams.loc[df_Teams['team'] == team, [Side + '_YCA']] = df_Teams[df_Teams['team'] == team][Side + '_YCA'].values[
                                                                  0] + AY  # Yellow Cards Agienst
    df_Teams.loc[df_Teams['team'] == team, [Side + '_RCF']] = df_Teams[df_Teams['team'] == team][Side + '_RCF'].values[
                                                                  0] + HR  # Red Cards For
    df_Teams.loc[df_Teams['team'] == team, [Side + '_RCA']] = df_Teams[df_Teams['team'] == team][Side + '_RCA'].values[
                                                                  0] + AR  # Red Cards Agienst


def updateRefTable(Ref, HY, AY, HR, AR, HF, AF):
    global df_Referee

    RG, YP, RP, FKC = getRefStats(Ref)

    df_Referee.loc[df_Referee['Name'] == Ref, ['Games']] = RG + 1
    df_Referee.loc[df_Referee['Name'] == Ref, ['YD']] = YP + HY + AY  # Yellow Drawn
    df_Referee.loc[df_Referee['Name'] == Ref, ['RD']] = RP + HR + AR  # Red Drawn
    df_Referee.loc[df_Referee['Name'] == Ref, ['FKC']] = FKC + HF + AF  # Free kicks Calls
    df_Referee.loc[df_Referee['Name'] == Ref, ['YPG']] = df_Referee[df_Referee['Name'] == Ref]['YD'].values[0] / (
            RG + 1)  # Yellow Per Game
    df_Referee.loc[df_Referee['Name'] == Ref, ['RPG']] = df_Referee[df_Referee['Name'] == Ref]['RD'].values[0] / (
            RG + 1)  # Red Per Game
    df_Referee.loc[df_Referee['Name'] == Ref, ['FKCPG']] = df_Referee[df_Referee['Name'] == Ref]['FKC'].values[0] / (
            RG + 1)  # Free kicks Calls Per Game


def updateDataTable(HT, AT, Ref, row):
    global data

    # Each side data
    HGames, H_FTWPG, H_FTDPG, H_FTLPG, H_HTWPG, H_HTDPG, H_HTLPG, H_FTGFPG, H_FTGAPG, H_HTGFPG, H_HTGAPG, H_SFPG, H_SAPG, H_SoTFPG, H_SoTAPG, H_CFPG, H_CAPG, H_FFPG, H_FAPG, H_YCFPG, H_YCAPG, H_RCFPG, H_RCAPG, AGames, A_FTWPG, A_FTDPG, A_FTLPG, A_HTWPG, A_HTDPG, A_HTLPG, A_FTGFPG, A_FTGAPG, A_HTGFPG, A_HTGAPG, A_SFPG, A_SAPG, A_SoTFPG, A_SoTAPG, A_CFPG, A_CAPG, A_FFPG, A_FAPG, A_YCFPG, A_YCAPG, A_RCFPG, A_RCAPG = getTeamsStats(
        HT, AT)

    # For total data
    HGames2, H_FTWPG2, H_FTDPG2, H_FTLPG2, H_HTWPG2, H_HTDPG2, H_HTLPG2, H_FTGFPG2, H_FTGAPG2, H_HTGFPG2, H_HTGAPG2, H_SFPG2, H_SAPG2, H_SoTFPG2, H_SoTAPG2, H_CFPG2, H_CAPG2, H_FFPG2, H_FAPG2, H_YCFPG2, H_YCAPG2, H_RCFPG2, H_RCAPG2, AGames2, A_FTWPG2, A_FTDPG2, A_FTLPG2, A_HTWPG2, A_HTDPG2, A_HTLPG2, A_FTGFPG2, A_FTGAPG2, A_HTGFPG2, A_HTGAPG2, A_SFPG2, A_SAPG2, A_SoTFPG2, A_SoTAPG2, A_CFPG2, A_CAPG2, A_FFPG2, A_FAPG2, A_YCFPG2, A_YCAPG2, A_RCFPG2, A_RCAPG2 = getTeamsStats(
        AT, HT)

    # Previues Result for both teams and Previues Encounter
    HPR1, HPR2, HPR3, HPR4, HPR5 = getLastFiveGames(HT, 'Home')
    APR1, APR2, APR3, APR4, APR5 = getLastFiveGames(AT, 'Away')
    PE1, PE2, PE3, PE4, PE5 = getLastFiveEncounter(HT, AT)

    # Ref stats
    # RG, YP, RP, FKC = getRefStats(Ref)

    # In case games is zero and we cant divide
    if HGames == 0:
        HomeCorrection = 0
        HGames = 1
    else:
        HomeCorrection = HGames
    if AGames == 0:
        AwayCorrection = 0
        AGames = 1
    else:
        AwayCorrection = AGames

    if HGames2 == 0:
        HomeCorrection2 = 0
        HGames2 = 1
    else:
        HomeCorrection2 = HGames2
    if AGames2 == 0:
        AwayCorrection2 = 0
        AGames2 = 1
    else:
        AwayCorrection2 = AGames2

    RGC = 1
    # if RG > 0:
    # RGC = RG

    data = data.append({'Date': row['Date'], 'HomeTeam': HT, 'AwayTeam': AT, 'FTGD': (row['FTHG'] - row['FTAG'])
                           , 'FTR': row['FTR'], 'HTGD': row['HTHG'] - row['HTAG'], 'HTR': row['HTR']  # ,'Referee':Ref

                        # Total stats - Home Team Total(Both home and away history stats)
                           , 'TH_Games': HomeCorrection + AwayCorrection2
                           , 'TH_FTW': (H_FTWPG + A_FTWPG2)  # Total FT Win
                           , 'TH_FTD': (H_FTDPG + A_FTDPG2)  # Total FT Draw
                           , 'TH_FTL': (H_FTLPG + A_FTLPG2)  # Total FT Loss
                           , 'TH_HTW': (H_HTWPG + A_HTWPG2)  # Total HT Win
                           , 'TH_HTD': (H_HTDPG + A_HTDPG2)  # Total HT Draw
                           , 'TH_HTL': (H_HTLPG + A_HTLPG2)  # Total HT Loss
                           , 'TH_FTGF': (H_FTGFPG + A_FTGFPG2)  # Total FT Goal For
                           , 'TH_FTGA': (H_FTGAPG + A_FTGAPG2)  # Total FT Goal Agienst
                           , 'TH_FTGD': ((H_FTGFPG - H_FTGAPG) + (A_FTGFPG2 - A_FTGAPG2))  # Total FT Goal Diffrence
                           , 'TH_HTGF': (H_HTGFPG + A_HTGFPG2)  # Total HT Goal For
                           , 'TH_HTGA': (H_HTGAPG + A_HTGAPG2)  # Total HT Goal Agienst
                           , 'TH_HTGD': ((H_HTGFPG - H_HTGAPG) + (A_HTGFPG2 - A_HTGAPG2))  # Total HT Goal Diffrence
                           , 'TH_SF': (H_SFPG + A_SFPG2)  # Total Shot For
                           , 'TH_SA': (H_SAPG + A_SAPG2)  # Total Shot Agienst
                           , 'TH_SoTF': (H_SoTFPG + A_SoTFPG2)  # Total Shot on Target For
                           , 'TH_SoTA': (H_SoTAPG + A_SoTAPG2)  # Total Shot on Target Agienst
                           , 'TH_CF': (H_CFPG + A_CFPG2)  # Total Corners For
                           , 'TH_CA': (H_CAPG + A_CAPG2)  # Total Corners Agienst
                           , 'TH_FF': (H_FFPG + A_FFPG2)  # Total Fouls For
                           , 'TH_FA': (H_FAPG + A_FAPG2)  # Total Fouls Agienst
                           , 'TH_YCF': (H_YCFPG + A_YCFPG2)  # Total Yellow Card For
                           , 'TH_YCA': (H_YCAPG + A_YCAPG2)  # Total Yellow Card Agienst
                           , 'TH_RCF': (H_RCFPG + A_RCFPG2)  # Total Red Card For
                           , 'TH_RCA': (H_RCAPG + A_RCAPG2)  # Total Red Card Agienst

                        # Per Game stats - Home Team Total(Both home and away history stats)
                           , 'TH_FTWPG': (H_FTWPG + A_FTWPG2) / (HGames + AGames2)  # Total FT Win Per Game
                           , 'TH_FTDPG': (H_FTDPG + A_FTDPG2) / (HGames + AGames2)  # Total FT Draw Per Game
                           , 'TH_FTLPG': (H_FTLPG + A_FTLPG2) / (HGames + AGames2)  # Total FT Loss Per Game
                           , 'TH_HTWPG': (H_HTWPG + A_HTWPG2) / (HGames + AGames2)  # Total HT Win Per Game
                           , 'TH_HTDPG': (H_HTDPG + A_HTDPG2) / (HGames + AGames2)  # Total HT Draw Per Game
                           , 'TH_HTLPG': (H_HTLPG + A_HTLPG2) / (HGames + AGames2)  # Total HT Loss Per Game
                           , 'TH_FTGFPG': (H_FTGFPG + A_FTGFPG2) / (HGames + AGames2)  # Total FT Goal For
                           , 'TH_FTGAPG': (H_FTGAPG + A_FTGAPG2) / (HGames + AGames2)  # Total FT Goal Agienst
                           , 'TH_FTGDPG': ((H_FTGFPG - H_FTGAPG) + (A_FTGFPG2 - A_FTGAPG2)) / (HGames + AGames2)
                        # Total FT Goal Diffrence
                           , 'TH_HTGFPG': (H_HTGFPG + A_HTGFPG2) / (HGames + AGames2)  # Total HT Goal For
                           , 'TH_HTGAPG': (H_HTGAPG + A_HTGAPG2) / (HGames + AGames2)  # Total HT Goal Agienst
                           , 'TH_HTGDPG': ((H_HTGFPG - H_HTGAPG) + (A_HTGFPG2 - A_HTGAPG2)) / (HGames + AGames2)
                        # Total HT Goal Diffrence
                           , 'TH_SFPG': (H_SFPG + A_SFPG2) / (HGames + AGames2)  # Total Shot For Per Game
                           , 'TH_SAPG': (H_SAPG + A_SAPG2) / (HGames + AGames2)  # Total Shot Agienst Per Game
                           , 'TH_SoTFPG': (H_SoTFPG + A_SoTFPG2) / (HGames + AGames2)
                        # Total Shot on Target For Per Game
                           , 'TH_SoTAPG': (H_SoTAPG + A_SoTAPG2) / (HGames + AGames2)
                        # Total Shot on Target Agienst Per Game
                           , 'TH_CFPG': (H_CFPG + A_CFPG2) / (HGames + AGames2)  # Total Corners For Per Game
                           , 'TH_CAPG': (H_CAPG + A_CAPG2) / (HGames + AGames2)  # Total Corners Agienst Per Game
                           , 'TH_FFPG': (H_FFPG + A_FFPG2) / (HGames + AGames2)  # Total Fouls For Per Game
                           , 'TH_FAPG': (H_FAPG + A_FAPG2) / (HGames + AGames2)  # Total Fouls Agienst Per Game
                           , 'TH_YCFPG': (H_YCFPG + A_YCFPG2) / (HGames + AGames2)  # Total Yellow Card For Per Game
                           , 'TH_YCAPG': (H_YCAPG + A_YCAPG2) / (HGames + AGames2)  # Total Yellow Card Agienst Per Game
                           , 'TH_RCFPG': (H_RCFPG + A_RCFPG2) / (HGames + AGames2)  # Total Red Card For Per Game
                           , 'TH_RCAPG': (H_RCAPG + A_RCAPG2) / (HGames + AGames2)
                        # Total Red Card Agienst Per Game

                        # Side stats - Home Team
                           , 'H_Games': HomeCorrection
                           , 'H_FTW': H_FTWPG  # FT Win
                           , 'H_FTD': H_FTDPG  # FT Draw
                           , 'H_FTL': H_FTLPG  # FT Loss
                           , 'H_HTW': H_HTWPG  # HT Win
                           , 'H_HTD': H_HTDPG  # HT Draw
                           , 'H_HTL': H_HTLPG  # HT Loss
                           , 'H_FTGF': H_FTGFPG  # FT Goal For
                           , 'H_FTGA': H_FTGAPG  # FT Goal Agienst
                           , 'H_FTGD': (H_FTGFPG - H_FTGAPG)  # FT Goal Diffrence
                           , 'H_HTGF': H_HTGFPG  # HT Goal For
                           , 'H_HTGA': H_HTGAPG  # HT Goal Agienst
                           , 'H_HTGD': (H_HTGFPG - H_HTGAPG)  # HT Goal Diffrence
                           , 'H_SF': H_SFPG  # Shot For
                           , 'H_SA': H_SAPG  # Shot Agienst
                           , 'H_SoTF': H_SoTFPG  # Shot on Target For
                           , 'H_SoTA': H_SoTAPG  # Shot on Target Agienst
                           , 'H_CF': H_CFPG  # Corners For
                           , 'H_CA': H_CAPG  # Corners Agienst
                           , 'H_FF': H_FFPG  # Fouls For
                           , 'H_FA': H_FAPG  # Fouls Agienst
                           , 'H_YCF': H_YCFPG  # Yellow Card For
                           , 'H_YCA': H_YCAPG  # Yellow Card Agienst
                           , 'H_RCF': H_RCFPG  # Red Card For
                           , 'H_RCA': H_RCAPG  # Red Card Agienst

                        # Per Game stats - Home Team
                           , 'H_FTWPG': H_FTWPG / HGames  # FT Win Per Game
                           , 'H_FTDPG': H_FTDPG / HGames  # FT Draw Per Game
                           , 'H_FTLPG': H_FTLPG / HGames  # FT Loss Per Game
                           , 'H_HTWPG': H_HTWPG / HGames  # HT Win Per Game
                           , 'H_HTDPG': H_HTDPG / HGames  # HT Draw Per Game
                           , 'H_HTLPG': H_HTLPG / HGames  # HT Loss Per Game
                           , 'H_FTGFPG': H_FTGFPG / HGames  # FT Goal For
                           , 'H_FTGAPG': H_FTGAPG / HGames  # FT Goal Agienst
                           , 'H_FTGDPG': (H_FTGFPG - H_FTGAPG) / HGames  # FT Goal Diffrence
                           , 'H_HTGFPG': H_HTGFPG / HGames  # HT Goal For
                           , 'H_HTGAPG': H_HTGAPG / HGames  # HT Goal Agienst
                           , 'H_HTGDPG': (H_HTGFPG - H_HTGAPG) / HGames  # HT Goal Diffrence
                           , 'H_SFPG': H_SFPG / HGames  # Shot For Per Game
                           , 'H_SAPG': H_SAPG / HGames  # Shot Agienst Per Game
                           , 'H_SoTFPG': H_SoTFPG / HGames  # Shot on Target For Per Game
                           , 'H_SoTAPG': H_SoTAPG / HGames  # Shot on Target Agienst Per Game
                           , 'H_CFPG': H_CFPG / HGames  # Corners For Per Game
                           , 'H_CAPG': H_CAPG / HGames  # Corners Agienst Per Game
                           , 'H_FFPG': H_FFPG / HGames  # Fouls For Per Game
                           , 'H_FAPG': H_FAPG / HGames  # Fouls Agienst Per Game
                           , 'H_YCFPG': H_YCFPG / HGames  # Yellow Card For Per Game
                           , 'H_YCAPG': H_YCAPG / HGames  # Yellow Card Agienst Per Game
                           , 'H_RCFPG': H_RCFPG / HGames  # Red Card For Per Game
                           , 'H_RCAPG': H_RCAPG / HGames  # Red Card Agienst Per Game

                        # Total stats - Away Team Total(Both home and away history stats)
                           , 'TA_Games': HomeCorrection2 + AwayCorrection
                           , 'TA_FTW': (H_FTWPG2 + A_FTWPG)  # Total FT Win
                           , 'TA_FTD': (H_FTDPG2 + A_FTDPG)  # Total FT Draw
                           , 'TA_FTL': (H_FTLPG2 + A_FTLPG)  # Total FT Loss
                           , 'TA_HTW': (H_HTWPG2 + A_HTWPG)  # Total HT Win
                           , 'TA_HTD': (H_HTDPG2 + A_HTDPG)  # Total HT Draw
                           , 'TA_HTL': (H_HTLPG2 + A_HTLPG)  # Total HT Loss
                           , 'TA_FTGF': (H_FTGFPG2 + A_FTGFPG)  # Total FT Goal For
                           , 'TA_FTGA': (H_FTGAPG2 + A_FTGAPG)  # Total FT Goal Agienst
                           , 'TA_FTGD': ((H_FTGFPG2 - H_FTGAPG2) + (A_FTGFPG - A_FTGAPG))  # Total FT Goal Diffrence
                           , 'TA_HTGF': (H_HTGFPG2 + A_HTGFPG)  # Total HT Goal For
                           , 'TA_HTGA': (H_HTGAPG2 + A_HTGAPG)  # Total HT Goal Agienst
                           , 'TA_HTGD': ((H_HTGFPG2 - H_HTGAPG2) + (A_HTGFPG - A_HTGAPG))  # Total HT Goal Diffrence
                           , 'TA_SF': (H_SFPG2 + A_SFPG)  # Total Shot For
                           , 'TA_SA': (H_SAPG2 + A_SAPG)  # Total Shot Agienst
                           , 'TA_SoTF': (H_SoTFPG2 + A_SoTFPG)  # Total Shot on Target For
                           , 'TA_SoTA': (H_SoTAPG2 + A_SoTAPG)  # Total Shot on Target Agienst
                           , 'TA_CF': (H_CFPG2 + A_CFPG)  # Total Corners For
                           , 'TA_CA': (H_CAPG2 + A_CAPG)  # Total Corners Agienst
                           , 'TA_FF': (H_FFPG2 + A_FFPG)  # Total Fouls For
                           , 'TA_FA': (H_FAPG2 + A_FAPG)  # Total Fouls Agienst
                           , 'TA_YCF': (H_YCFPG2 + A_YCFPG)  # Total Yellow Card For
                           , 'TA_YCA': (H_YCAPG2 + A_YCAPG)  # Total Yellow Card Agienst
                           , 'TA_RCF': (H_RCFPG2 + A_RCFPG)  # Total Red Card For
                           , 'TA_RCA': (H_RCAPG2 + A_RCAPG)  # Total Red Card Agienst

                        # Per Game stats - Away Team Total(Both home and away history stats)
                           , 'TA_FTWPG': (H_FTWPG2 + A_FTWPG) / (HGames2 + AGames)  # Total FT Win Per Game
                           , 'TA_FTDPG': (H_FTDPG2 + A_FTDPG) / (HGames2 + AGames)  # Total FT Draw Per Game
                           , 'TA_FTLPG': (H_FTLPG2 + A_FTLPG) / (HGames2 + AGames)  # Total FT Loss Per Game
                           , 'TA_HTWPG': (H_HTWPG2 + A_HTWPG) / (HGames2 + AGames)  # Total HT Win Per Game
                           , 'TA_HTDPG': (H_HTDPG2 + A_HTDPG) / (HGames2 + AGames)  # Total HT Draw Per Game
                           , 'TA_HTLPG': (H_HTLPG2 + A_HTLPG) / (HGames2 + AGames)  # Total HT Loss Per Game
                           , 'TA_FTGFPG': (H_FTGFPG2 + A_FTGFPG) / (HGames2 + AGames)  # Total FT Goal For
                           , 'TA_FTGAPG': (H_FTGAPG2 + A_FTGAPG) / (HGames2 + AGames)  # Total FT Goal Agienst
                           , 'TA_FTGDPG': ((H_FTGFPG2 - H_FTGAPG2) + (A_FTGFPG - A_FTGAPG)) / (HGames2 + AGames)
                        # Total FT Goal Diffrence
                           , 'TA_HTGFPG': (H_HTGFPG2 + A_HTGFPG) / (HGames2 + AGames)  # Total HT Goal For
                           , 'TA_HTGAPG': (H_HTGAPG2 + A_HTGAPG) / (HGames2 + AGames)  # Total HT Goal Agienst
                           , 'TA_HTGDPG': ((H_HTGFPG2 - H_HTGAPG2) + (A_HTGFPG - A_HTGAPG)) / (HGames2 + AGames)
                        # Total HT Goal Diffrence
                           , 'TA_SFPG': (H_SFPG2 + A_SFPG) / (HGames2 + AGames)  # Total Shot For Per Game
                           , 'TA_SAPG': (H_SAPG2 + A_SAPG) / (HGames2 + AGames)  # Total Shot Agienst Per Game
                           , 'TA_SoTFPG': (H_SoTFPG2 + A_SoTFPG) / (HGames2 + AGames)
                        # Total Shot on Target For Per Game
                           , 'TA_SoTAPG': (H_SoTAPG2 + A_SoTAPG) / (HGames2 + AGames)
                        # Total Shot on Target Agienst Per Game
                           , 'TA_CFPG': (H_CFPG2 + A_CFPG) / (HGames2 + AGames)  # Total Corners For Per Game
                           , 'TA_CAPG': (H_CAPG2 + A_CAPG) / (HGames2 + AGames)  # Total Corners Agienst Per Game
                           , 'TA_FFPG': (H_FFPG2 + A_FFPG) / (HGames2 + AGames)  # Total Fouls For Per Game
                           , 'TA_FAPG': (H_FAPG2 + A_FAPG) / (HGames2 + AGames)  # Total Fouls Agienst Per Game
                           , 'TA_YCFPG': (H_YCFPG2 + A_YCFPG) / (HGames2 + AGames)  # Total Yellow Card For Per Game
                           , 'TA_YCAPG': (H_YCAPG2 + A_YCAPG) / (HGames2 + AGames)  # Total Yellow Card Agienst Per Game
                           , 'TA_RCFPG': (H_RCFPG2 + A_RCFPG) / (HGames2 + AGames)  # Total Red Card For Per Game
                           , 'TA_RCAPG': (H_RCAPG2 + A_RCAPG) / (HGames2 + AGames)  # Total Red Card Agienst Per Game

                        # side stats - Away Team
                           , 'A_Games': AwayCorrection
                           , 'A_FTW': A_FTWPG  # FT Win Per Game
                           , 'A_FTD': A_FTWPG  # FT Draw Per Game
                           , 'A_FTL': A_FTLPG  # FT Loss Per Game
                           , 'A_HTW': A_HTWPG  # HT Win Per Game
                           , 'A_HTD': A_HTDPG  # HT Draw Per Game
                           , 'A_HTL': A_HTLPG  # HT Loss Per Game
                           , 'A_FTGF': A_FTGFPG  # FT Goal For
                           , 'A_FTGA': A_FTGAPG  # FT Goal Agienst
                           , 'A_FTGD': (A_FTGFPG - A_FTGAPG)  # FT Goal Diffrence
                           , 'A_HTGF': A_HTGFPG  # HT Goal For
                           , 'A_HTGA': A_HTGAPG  # HT Goal Agienst
                           , 'A_HTGD': (A_HTGFPG - A_HTGAPG)  # HT Goal Diffrence
                           , 'A_SF': A_SFPG  # Shot For Per Game
                           , 'A_SA': A_SAPG  # Shot Agienst Per Game
                           , 'A_SoTF': A_SoTFPG  # Shot on Target For Per Game
                           , 'A_SoTA': A_SoTAPG  # Shot on Target Agienst Per Game
                           , 'A_CF': A_CFPG  # Corners For Per Game
                           , 'A_CA': A_CAPG  # Corners Agienst Per Game
                           , 'A_FF': A_FFPG  # Fouls For Per Game
                           , 'A_FA': A_FAPG  # Fouls Agienst Per Game
                           , 'A_YCF': A_YCFPG  # Yellow Card For Per Game
                           , 'A_YCA': A_YCAPG  # Yellow Card Agienst Per Game
                           , 'A_RCF': A_RCFPG  # Red Card For Per Game
                           , 'A_RCA': A_RCAPG  # Red Card Agienst Per Game

                        # Per Game stats - Away Team
                           , 'A_FTWPG': A_FTWPG / AGames  # FT Win Per Game
                           , 'A_FTDPG': A_FTWPG / AGames  # FT Draw Per Game
                           , 'A_FTLPG': A_FTLPG / AGames  # FT Loss Per Game
                           , 'A_HTWPG': A_HTWPG / AGames  # HT Win Per Game
                           , 'A_HTDPG': A_HTDPG / AGames  # HT Draw Per Game
                           , 'A_HTLPG': A_HTLPG / AGames  # HT Loss Per Game
                           , 'A_FTGFPG': A_FTGFPG / AGames  # FT Goal For
                           , 'A_FTGAPG': A_FTGAPG / AGames  # FT Goal Agienst
                           , 'A_FTGDPG': (A_FTGFPG - A_FTGAPG) / AGames  # FT Goal Diffrence
                           , 'A_HTGFPG': A_HTGFPG / AGames  # HT Goal For
                           , 'A_HTGAPG': A_HTGAPG / AGames  # HT Goal Agienst
                           , 'A_HTGDPG': (A_HTGFPG - A_HTGAPG) / AGames  # HT Goal Diffrence
                           , 'A_SFPG': A_SFPG / AGames  # Shot For Per Game
                           , 'A_SAPG': A_SAPG / AGames  # Shot Agienst Per Game
                           , 'A_SoTFPG': A_SoTFPG / AGames  # Shot on Target For Per Game
                           , 'A_SoTAPG': A_SoTAPG / AGames  # Shot on Target Agienst Per Game
                           , 'A_CFPG': A_CFPG / AGames  # Corners For Per Game
                           , 'A_CAPG': A_CAPG / AGames  # Corners Agienst Per Game
                           , 'A_FFPG': A_FFPG / AGames  # Fouls For Per Game
                           , 'A_FAPG': A_FAPG / AGames  # Fouls Agienst Per Game
                           , 'A_YCFPG': A_YCFPG / AGames  # Yellow Card For Per Game
                           , 'A_YCAPG': A_YCAPG / AGames  # Yellow Card Agienst Per Game
                           , 'A_RCFPG': A_RCFPG / AGames  # Red Card For Per Game
                           , 'A_RCAPG': A_RCAPG / AGames  # Red Card Agienst Per Game

                        # HPR = Home Previues Result, APR = Away Previues Result, PE = Previues Encounter
                           , 'HPR1': HPR1, 'HPR2': HPR2, 'HPR3': HPR3, 'HPR4': HPR4, 'HPR5': HPR5
                           , 'APR1': APR1, 'APR2': APR2, 'APR3': APR3, 'APR4': APR4, 'APR5': APR5
                           , 'PE1': PE1, 'PE2': PE2, 'PE3': PE3, 'PE4': PE4, 'PE5': PE5

                        # Referee Per Game stats
                        # ,'RefGames':RG, 'RefYD':YP, 'RefRD':RP, 'RefFKC':FKC, 'RefYDPG':YP/RGC, 'RefRDPG':RP/RGC, 'RefFKCPG':FKC/RGC

                        # Bet stats
                           , 'B365H': row['B365H'], 'B365D': row['B365D'], 'B365A': row['B365A'], 'BWH': row['BWH'],
                        'BWD': row['BWD']
                           , 'BWA': row['BWA'], 'IWH': row['IWH'], 'IWD': row['IWD'], 'IWA': row['IWA'],
                        'PSH': row['PSH'], 'PSD': row['PSD']
                           , 'PSA': row['PSA'], 'PSCH': row['PSCH'], 'PSCD': row['PSCD'], 'PSCA': row['PSCA']
                           , 'WHH': row['WHH'], 'WHD': row['WHD'], 'WHA': row['WHA'], 'VCH': row['VCH'],
                        'VCD': row['VCD'], 'VCA': row['VCA']

                        # Other Stats - TODO ???
                        # df_Teams.team['T'] #Titels
                        # df_Teams.team['RU'] #Runner Ups
                        # df_Teams.team['CC'] #Current Champions
                        # df_Teams.team['CRU'] #Current Runner Up

                        }, ignore_index=True)


def getTeamsStats(HT, AT):
    global df_Teams

    return (df_Teams[df_Teams['team'] == HT]['H_Games'].values[0],

            df_Teams[df_Teams['team'] == HT]['H_FTWins'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTDraws'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTLost'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTWins'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTDraws'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTLost'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTGF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTGA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTGF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTGA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SoTF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SoTA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_CF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_CA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_YCF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_YCA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_RCF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_RCA'].values[0],
            df_Teams[df_Teams['team'] == HT]['A_Games'].values[0],

            df_Teams[df_Teams['team'] == AT]['A_FTWins'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTDraws'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTLost'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTWins'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTDraws'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTLost'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTGF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTGA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTGF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTGA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SoTF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SoTA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_CF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_CA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_YCF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_YCA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_RCF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_RCA'].values[0])


def getTeamsStats(HT, AT):
    global df_Teams

    return (df_Teams[df_Teams['team'] == HT]['H_Games'].values[0],

            df_Teams[df_Teams['team'] == HT]['H_FTWins'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTDraws'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTLost'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTWins'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTDraws'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTLost'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTGF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FTGA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTGF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_HTGA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SoTF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_SoTA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_CF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_CA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_FA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_YCF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_YCA'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_RCF'].values[0],
            df_Teams[df_Teams['team'] == HT]['H_RCA'].values[0],
            df_Teams[df_Teams['team'] == HT]['A_Games'].values[0],

            df_Teams[df_Teams['team'] == AT]['A_FTWins'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTDraws'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTLost'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTWins'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTDraws'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTLost'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTGF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FTGA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTGF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_HTGA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SoTF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_SoTA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_CF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_CA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_FA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_YCF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_YCA'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_RCF'].values[0],
            df_Teams[df_Teams['team'] == AT]['A_RCA'].values[0])


def getLastFiveGames(team, side):
    global data

    N = 5
    LastFiveHomeGames = data[data['HomeTeam'] == team][-N:]
    LastFiveAwayGames = data[data['AwayTeam'] == team][-N:]

    LastFiveHomeGames = LastFiveHomeGames.append(LastFiveAwayGames)
    LastFiveHomeGames = LastFiveHomeGames.sort_index()

    LastFiveHomeGames = LastFiveHomeGames[-N:]
    if len(LastFiveHomeGames) > 4:
        PR1 = LastFiveHomeGames["FTGD"].iloc[4]
    else:
        PR1 = 0
    if len(LastFiveHomeGames) > 3:
        PR2 = LastFiveHomeGames["FTGD"].iloc[3]
    else:
        PR2 = 0
    if len(LastFiveHomeGames) > 2:
        PR3 = LastFiveHomeGames["FTGD"].iloc[2]
    else:
        PR3 = 0
    if len(LastFiveHomeGames) > 1:
        PR4 = LastFiveHomeGames["FTGD"].iloc[1]
    else:
        PR4 = 0
    if len(LastFiveHomeGames) > 0:
        PR5 = LastFiveHomeGames["FTGD"].iloc[0]
    else:
        PR5 = 0

    listofPR = [PR1, PR2, PR3, PR4, PR5]
    for index in range(len(listofPR)):
        if len(LastFiveHomeGames) > (4 - index):
            if ((side == 'Home' and LastFiveHomeGames["HomeTeam"].iloc[4 - index] != team) or
                    (side == 'Away' and LastFiveHomeGames["AwayTeam"].iloc[4 - index] != team)):
                listofPR[index] = listofPR[index] * (-1)

    return listofPR[0], listofPR[1], listofPR[2], listofPR[3], listofPR[4]


def getLastFiveEncounter(HT, AT):
    global data

    N = 5
    LastFiveHomeGames = data.loc[data['HomeTeam'] == HT]
    LastFiveHomeGames = LastFiveHomeGames.loc[LastFiveHomeGames['AwayTeam'] == AT][-N:]

    LastFiveAwayGames = data.loc[data['HomeTeam'] == AT]
    LastFiveAwayGames = LastFiveAwayGames.loc[LastFiveAwayGames['AwayTeam'] == HT][-N:]

    LastFiveHomeGames = LastFiveHomeGames.append(LastFiveAwayGames)
    LastFiveHomeGames = LastFiveHomeGames.sort_index()

    LastFiveHomeGames = LastFiveHomeGames[-N:]
    if len(LastFiveHomeGames) > 4:
        PE1 = LastFiveHomeGames["FTGD"].iloc[4]
    else:
        PE1 = 0
    if len(LastFiveHomeGames) > 3:
        PE2 = LastFiveHomeGames["FTGD"].iloc[3]
    else:
        PE2 = 0
    if len(LastFiveHomeGames) > 2:
        PE3 = LastFiveHomeGames["FTGD"].iloc[2]
    else:
        PE3 = 0
    if len(LastFiveHomeGames) > 1:
        PE4 = LastFiveHomeGames["FTGD"].iloc[1]
    else:
        PE4 = 0
    if len(LastFiveHomeGames) > 0:
        PE5 = LastFiveHomeGames["FTGD"].iloc[0]
    else:
        PE5 = 0

    listofPE = [PE1, PE2, PE3, PE4, PE5]
    for index in range(len(listofPE)):
        if len(LastFiveHomeGames) > (4 - index):
            if LastFiveHomeGames['HomeTeam'].iloc[4 - index] == AT:
                listofPE[index] = listofPE[index] * (-1)

    return listofPE[0], listofPE[1], listofPE[2], listofPE[3], listofPE[4]


def games(df):
    t1 = time()
    for index, row in df.iterrows():
        print('Game ', index)
        t2 = time()
        HT = row['HomeTeam']
        AT = row['AwayTeam']
        Ref = row["Referee"]

        # Add new team - take 0.01 sec
        for team in HT, AT:
            if df_Teams[df_Teams['team'] == team].empty:  # Add new team to table
                addTeam(team)

        # if df_Referee[df_Referee['Name'] == Ref].empty: #Add new Referee to table
        # addRef(Ref)

        # Update Data Table - take 0.1 sec
        updateDataTable(HT, AT, Ref, row)

        # Update Referee Table
        # updateRefTable(Ref, row['HY'], row['AY'], row['HR'], row['AR'], row['HF'], row['AF'])

        # Update Teams Table - takes 0.1 sec
        for team in HT, AT:
            if team == HT:  # Home team
                Side = 'H'
                OtherSide = 'A'
            else:  # Away team
                Side = 'A'
                OtherSide = 'H'

            updateTeamsTable(Side, OtherSide, row, team)

        print("Finished in ", time() - t2, " seconds")
    print((time() - t1) / 3600, ' Hours')


# Leagues Stats Reading
def readStats():
    mydf = pd.DataFrame()
    for dirname, dirnames, filenames in os.walk('.'):
        for subdirname in dirnames:
            if subdirname != '.ipynb_checkpoints':
                for file in os.listdir(subdirname):
                    df2 = pd.read_csv(subdirname + "\\" + file, error_bad_lines=False, encoding='windows-1254')
                    mydf = mydf.append(df2, sort=False, ignore_index=True)
    return mydf


def saveStats(mydf):
    mydf = mydf.fillna(0)
    GamesName = 'GamesBeforDataManipulation.csv'
    mydf.to_csv(GamesName, index=False, sep=',')
    # df = pd.read_csv(GamesName)
    mydf.describe()


# Create my Own Stats Table
def Initilize():
    # Intilize
    data = pd.DataFrame(
        {'Date': {}, 'HomeTeam': {}, 'AwayTeam': {}, 'FTGD': {}, 'FTR': {}, 'HTGD': {}, 'HTR': {}  # ,'Referee':{}

            , 'TH_Games': {}, 'TH_FTW': {}, 'TH_FTD': {}, 'TH_FTL': {}, 'TH_HTW': {}, 'TH_HTD': {}, 'TH_HTL': {},
         'TH_FTGF': {}
            , 'TH_FTGA': {}, 'TH_FTGD': {}, 'TH_HTGF': {}, 'TH_HTGA': {}, 'TH_HTGD': {}, 'TH_SF': {}, 'TH_SA': {},
         'TH_SoTF': {}
            , 'TH_SoTA': {}, 'TH_CF': {}, 'TH_CA': {}, 'TH_FF': {}, 'TH_FA': {}, 'TH_YCF': {}, 'TH_YCA': {},
         'TH_RCF': {}, 'TH_RCA': {}

            , 'TH_FTWPG': {}, 'TH_FTDPG': {}, 'TH_FTLPG': {}, 'TH_HTWPG': {}, 'TH_HTDPG': {}, 'TH_HTLPG': {},
         'TH_FTGFPG': {}
            , 'TH_FTGAPG': {}, 'TH_FTGDPG': {}, 'TH_HTGFPG': {}, 'TH_HTGAPG': {}, 'TH_HTGDPG': {}, 'TH_SFPG': {},
         'TH_SAPG': {}
            , 'TH_SoTFPG': {}, 'TH_SoTAPG': {}, 'TH_CFPG': {}, 'TH_CAPG': {}, 'TH_FFPG': {}, 'TH_FAPG': {},
         'TH_YCFPG': {}
            , 'TH_YCAPG': {}, 'TH_RCFPG': {}, 'TH_RCAPG': {}

            , 'H_Games': {}, 'H_FTW': {}, 'H_FTD': {}, 'H_FTL': {}, 'H_HTW': {}, 'H_HTD': {}, 'H_HTL': {}, 'H_FTGF': {},
         'H_FTGA': {}
            , 'H_FTGD': {}, 'H_HTGF': {}, 'H_HTGA': {}, 'H_HTGD': {}, 'H_SF': {}, 'H_SA': {}, 'H_SoTF': {},
         'H_SoTA': {}, 'H_CF': {}
            , 'H_CA': {}, 'H_FF': {}, 'H_FA': {}, 'H_YCF': {}, 'H_YCA': {}, 'H_RCF': {}, 'H_RCA': {}

            , 'H_FTWPG': {}, 'H_FTDPG': {}, 'H_FTLPG': {}, 'H_HTWPG': {}, 'H_HTDPG': {}, 'H_HTLPG': {}, 'H_FTGFPG': {},
         'H_FTGAPG': {}
            , 'H_FTGDPG': {}, 'H_HTGFPG': {}, 'H_HTGAPG': {}, 'H_HTGDPG': {}, 'H_SFPG': {}, 'H_SAPG': {},
         'H_SoTFPG': {}, 'H_SoTAPG': {}
            , 'H_CFPG': {}, 'H_CAPG': {}, 'H_FFPG': {}, 'H_FAPG': {}, 'H_YCFPG': {}, 'H_YCAPG': {}, 'H_RCFPG': {},
         'H_RCAPG': {}

            , 'TA_Games': {}, 'TA_FTW': {}, 'TA_FTD': {}, 'TA_FTL': {}, 'TA_HTW': {}, 'TA_HTD': {}, 'TA_HTL': {},
         'TA_FTGF': {}
            , 'TA_FTGA': {}, 'TA_FTGD': {}, 'TA_HTGF': {}, 'TA_HTGA': {}, 'TA_HTGD': {}, 'TA_SF': {}, 'TA_SA': {},
         'TA_SoTF': {}
            , 'TA_SoTA': {}, 'TA_CF': {}, 'TA_CA': {}, 'TA_FF': {}, 'TA_FA': {}, 'TA_YCF': {}, 'TA_YCA': {},
         'TA_RCF': {}, 'TA_RCA': {}

            , 'TA_FTWPG': {}, 'TA_FTDPG': {}, 'TA_FTLPG': {}, 'TA_HTWPG': {}, 'TA_HTDPG': {}, 'TA_HTLPG': {},
         'TA_FTGFPG': {}
            , 'TA_FTGAPG': {}, 'TA_FTGDPG': {}, 'TA_HTGFPG': {}, 'TA_HTGAPG': {}, 'TA_HTGDPG': {}, 'TA_SFPG': {},
         'TA_SAPG': {}
            , 'TA_SoTFPG': {}, 'TA_SoTAPG': {}, 'TA_CFPG': {}, 'TA_CAPG': {}, 'TA_FFPG': {}, 'TA_FAPG': {},
         'TA_YCFPG': {}
            , 'TA_YCAPG': {}, 'TA_RCFPG': {}, 'TA_RCAPG': {}

            , 'A_Games': {}, 'A_FTW': {}, 'A_FTD': {}, 'A_FTL': {}, 'A_HTW': {}, 'A_HTD': {}, 'A_HTL': {}, 'A_FTGF': {},
         'A_FTGA': {}
            , 'A_FTGD': {}, 'A_HTGF': {}, 'A_HTGA': {}, 'A_HTGD': {}, 'A_SF': {}, 'A_SA': {}, 'A_SoTF': {},
         'A_SoTA': {}, 'A_CF': {}
            , 'A_CA': {}, 'A_FF': {}, 'A_FA': {}, 'A_YCF': {}, 'A_YCA': {}, 'A_RCF': {}, 'A_RCA': {}

            , 'A_FTWPG': {}, 'A_FTDPG': {}, 'A_FTLPG': {}, 'A_HTWPG': {}, 'A_HTDPG': {}, 'A_HTLPG': {}, 'A_FTGFPG': {},
         'A_FTGAPG': {}
            , 'A_FTGDPG': {}, 'A_HTGFPG': {}, 'A_HTGAPG': {}, 'A_HTGDPG': {}, 'A_SFPG': {}, 'A_SAPG': {}, 'A_SoTFPG': {}
            , 'A_SoTAPG': {}, 'A_CFPG': {}, 'A_CAPG': {}, 'A_FFPG': {}, 'A_FAPG': {}, 'A_YCFPG': {}, 'A_YCAPG': {},
         'A_RCFPG': {}, 'A_RCAPG': {}

            , 'HPR1': {}, 'HPR2': {}, 'HPR3': {}, 'HPR4': {}, 'HPR5': {}, 'APR1': {}, 'APR2': {}, 'APR3': {},
         'APR4': {}, 'APR5': {}
            , 'PE1': {}, 'PE2': {}, 'PE3': {}, 'PE4': {}, 'PE5': {}

         # ,'RefGames':{}, 'RefYD':{}, 'RefRD':{}, 'RefFKC':{}, 'RefYDPG':{}, 'RefRDPG':{}, 'RefFKCPG':{}

            , 'B365H': {}, 'B365D': {}, 'B365A': {}, 'BWH': {}, 'BWD': {}
            , 'BWA': {}, 'IWH': {}, 'IWD': {}, 'IWA': {}, 'WHH': {}, 'WHD': {}, 'WHA': {}, 'VCH': {}, 'VCD': {},
         'VCA': {}
            , 'PSH': {}, 'PSD': {}, 'PSA': {}, 'PSCH': {}, 'PSCD': {}, 'PSCA': {}

         })

    df_Teams = pd.DataFrame({"team": {}
                                , "H_Games": {}, "H_FTWins": {}, "H_FTDraws": {}, "H_FTLost": {}, "H_HTWins": {},
                             "H_HTDraws": {}, "H_HTLost": {}
                                , "H_FTGF": {}, "H_FTGA": {}, "H_FTGD": {}, "H_HTGF": {}, "H_HTGA": {}, "H_HTGD": {},
                             "H_SF": {}, "H_SA": {}
                                , "H_SoTF": {}, "H_SoTA": {}, "H_CF": {}, 'H_CA': {}, "H_FF": {}, "H_FA": {},
                             "H_YCF": {}, "H_YCA": {}, "H_RCF": {}
                                , "H_RCA": {}

                                , "A_Games": {}, "A_FTWins": {}, "A_FTDraws": {}, "A_FTLost": {}, "A_HTWins": {},
                             "A_HTDraws": {}, "A_HTLost": {}
                                , "A_FTGF": {}, "A_FTGA": {}, "A_FTGD": {}, "A_HTGF": {}, "A_HTGA": {}, "A_HTGD": {},
                             "A_SF": {}, "A_SA": {}
                                , "A_SoTF": {}, "A_SoTA": {}, "A_CF": {}, 'A_CA': {}, "A_FF": {}, "A_FA": {},
                             "A_YCF": {}, "A_YCA": {}, "A_RCF": {}
                                , "A_RCA": {}
                             })

    df_Referee = pd.DataFrame(
        {"Name": {}, "Games": {}, "YD": {}, "RD": {}, "FKC": {}, "YPG": {}, "RPG": {}, "FKCPG": {}})

    return data, df_Teams, df_Referee


def saveDataSet():
    global data

    data.to_csv("projectdata.csv", index=False, sep=',')
    data = pd.read_csv('projectdata.csv')
    data.head()


def save_df_Teams():
    global df_Teams

    df_Teams.to_csv("df_Teams.csv", index=False, sep=',')
    df_Teams = pd.read_csv('df_Teams.csv')
    df_Teams.head()


def save_df_Referee():
    global df_Referee
    df_Referee.to_csv("df_Referee.csv", index=False, sep=',')
    df_Referee = pd.read_csv('df_Referee.csv')
    df_Referee.head()


def getNewData(newGames):
    global data

    K = len(newGames)
    N = len(data) - K
    newData = data.iloc[N:]
    newData = newData.reset_index(drop=True)
    data = data[:N]
    return newData