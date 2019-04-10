cats_split = [['MSSubClass',
'20',	
'30',	
'40',	
'45',	
'50',	
'60',	
'70',	
'75',	
'80',	
'85',
'90',	
'120',	
'150',	
'160',	
'180',	
'190'],
['MSZoning',
'A',
'C (all)',
'FV',
'I',
'RH',
'RL',
'RP',
'RM'],
['Alley',
'Grvl',
'Pave',
'NA'],
['Utilities',
'AllPub',	
'NoSewr',
'NoSeWa',
'ELO'],
['LotConfig',
'Inside',
'Corner',
'CulDSac',
'FR2',
'FR3'],
['Neighborhood',
'Blmngtn',
'Blueste',
'BrDale',
'BrkSide',
'ClearCr',
'CollgCr',
'Crawfor',
'Edwards',
'Gilbert',
'IDOTRR',
'MeadowV',
'Mitchel',
'NAmes',
'NoRidge',
'NPkVill',
'NridgHt',
'NWAmes',
'OldTown',
'SWISU',
'Sawyer',
'SawyerW',
'Somerst',
'StoneBr',
'Timber',
'Veenker'],
['Condition1',
'Artery',
'Feedr',
'Norm',
'RRNn',
'RRAn',
'PosN',
'PosA',
'RRNe',
'RRAe'],
['Condition2',
'Artery',
'Feedr',
'Norm',
'RRNn',
'RRAn',
'PosN',
'PosA',
'RRNe',
'RRAe'],
['BldgType',
'1Fam',
'2FmCon',
'Duplx',
'TwnhsE',
'TwnhsI'],
['HouseStyle',
'1Story',
'1.5Fin',	
'1.5Unf',	
'2Story',
'2.5Fin',	
'2.5Unf',	
'SFoyer',
'SLvl'],
['RoofStyle',
'Flat',
'Gable',
'Gambrel',
'Hip',
'Mansard',
'Shed'],
['RoofMatl',
'ClyTile',
'CompShg',
'Membran',
'Metal',
'Roll',
'Tar&Grv',	
'WdShake',
'WdShngl'],
['Exterior1st',
'AsbShng',
'AsphShn',
'BrkComm',
'BrkFace',
'CBlock',
'CemntBd',
'HdBoard',
'ImStucc',
'MetalSd',
'Other',
'Plywood',
'PreCast',	
'Stone',
'Stucco',
'VinylSd',
'Wd Sdng',
'WdShing'],
['Exterior2nd',
'AsbShng',
'AsphShn',
'BrkComm',
'BrkFace',
'CBlock',
'CemntBd',
'HdBoard',
'ImStucc',
'MetalSd',
'Other',
'Plywood',
'PreCast',
'Stone',
'Stucco',
'VinylSd',
'Wd Sdng',
'WdShing'],
['MasVnrType',
'BrkCmn',
'BrkFace',
'CBlock',
'None',
'Stone'],
['Foundation',
'BrkTil',	
'CBlock',
'PConc',	
'Slab',
'Stone',
'Wood'],
['Heating',
'Floor',
'GasA',
'GasW',
'Grav',	
'OthW',
'Wall'],
['Electrical',
'SBrkr',
'FuseA',	
'FuseF',
'FuseP',	
'Mix'],
['GarageType',
'2Types',
'Attchd',
'Basment',
'BuiltIn',	
'CarPort',
'Detchd',
'NA'],
['PavedDrive',
'Y',
'P',
'N'],
['MiscFeature',
'Elev',
'Gar2',
'Othr',
'Shed',
'TenC',
'NA'],
['SaleType',
'WD',	
'CWD',	
'VWD',	
'New',
'COD',
'Con',
'ConLw',
'ConLI',
'ConLD',
'Oth'],
['SaleCondition',
'Normal',
'Abnorml',	
'AdjLand',
'Alloca',
'Family',
'Partial']]

cats_num = [{'name': 'Street',
'Grvl': 0,
'Pave': 1,
},
{'name': 'LotShape',
'Reg': 0,
'IR1': 1,
'IR2': 2,
'IR3': 3,
},
{'name': 'LandContour',
'Lvl': 0,
'Bnk': 1,
'HLS': 2,
'Low': 3,
},
{'name': 'LandSlope',
'Gtl': 0,
'Mod': 1,
'Sev': 2,
},
{'name': 'CentralAir',
'N': 0,
'Y': 1,
},
{'name': 'ExterQual',
'Ex': 4,
'Gd': 3,
'TA': 2,
'Fa': 1,
'Po': 0,
},
{'name': 'ExterCond',
'Ex': 4,
'Gd': 3,
'TA': 2,
'Fa': 1,
'Po': 0,
},
{'name': 'BsmtQual',
'Ex': 5,
'Gd': 4,
'TA': 3,
'Fa': 2,
'Po': 1,
'NA': 0,
},
{'name': 'BsmtCond',
'Ex': 5,
'Gd': 4,
'TA': 3,
'Fa': 2,
'Po': 1,
'NA': 0,
},
{'name': 'BsmtExposure',
'Gd': 4,
'Av': 3,
'Mn': 2,
'No': 1,
'NA': 0,
},
{'name': 'BsmtFinType1',
'GLQ': 6,
'ALQ': 5,
'BLQ': 4,
'Rec': 3,
'LwQ': 2,
'Unf': 1,
'NA': 0,
},
{'name': 'BsmtFinType2',
'GLQ': 6,
'ALQ': 5,
'BLQ': 4,
'Rec': 3,
'LwQ': 2,
'Unf': 1,
'NA': 0,
},
{'name': 'HeatingQC',
'Ex': 4,
'Gd': 3,
'TA': 2,
'Fa': 1,
'Po': 0,
},
{'name': 'KitchenQual',
'Ex': 4,
'Gd': 3,
'TA': 2,
'Fa': 1,
'Po': 0,
},
{'name': 'Functional',
'Typ': 0,
'Min1': 1,
'Min2': 2,
'Mod': 3,
'Maj1': 4,
'Maj2': 5,
'Sev': 6,
'Sal': 7,
},
{'name': 'FireplaceQu',
'Ex': 5,
'Gd': 4,
'TA': 3,
'Fa': 2,
'Po': 1,
'NA': 0,
},
{'name': 'GarageFinish',
'Fin': 3,
'RFn': 2,
'Unf': 1,
'NA': 0,
},
{'name': 'GarageQual',
'Ex': 5,
'Gd': 4,
'TA': 3,
'Fa': 2,
'Po': 1,
'NA': 0,
},
{'name': 'GarageCond',
'Ex': 5,
'Gd': 4,
'TA': 3,
'Fa': 2,
'Po': 1,
'NA': 0,
},
{'name': 'PoolQC',
'Ex': 4,
'Gd': 3,
'TA': 2,
'Fa': 1,
'NA': 0,
},
{'name': 'Fence',
'GdPrv': 4,
'MnPrv': 3,
'GdWo': 2,
'MnWw': 1,
'NA': 0,
}]

error_detect = [['BldgType',
'1Fam',
'2FmCon	',
'Duplx',
'TwnhsE',
'TwnhsI'],
['Exterior2nd',
'AsbShng',
'AsphShn',
'BrkComm',
'BrkFace',
'CBlock',
'CemntBd',
'HdBoard',
'ImStucc',
'MetalSd',
'Other',
'Plywood',
'PreCast',
'Stone',
'Stucco',
'VinylSd',
'Wd Sdng',
'WdShing'],
['MasVnrType',
'BrkCmn',
'BrkFace',
'CBlock',
'None',
'Stone'],
]