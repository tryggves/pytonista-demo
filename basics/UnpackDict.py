#
# Python unpacking
#

row = { "timestampAfterEpochMillis": "1701766800261", "messageJsonContent": [  {    "SPM_DG1": {      "SPESFUELCONS": 74.4942932128906    },    "SPM_DG2": {      "SPESFUELCONS": 74.4043197631836    },    "SPM_DG3": {      "SPESFUELCONS": 74.4279174804688    },    "SPM_DG4": {      "SPESFUELCONS": 74.4257659912109    },    "DG2": {      "POW": 2119.783203125    },    "DG4": {      "POW": 2089.57055664063    },    "DG3": {      "POW": 2117.40283203125    },    "861_004_0001_XT": {      "VALUE": 2089.57055664063    },    "861_003_0001_XT": {      "VALUE": 2117.40283203125    },    "861_002_0001_XT": {      "VALUE": 2107.6982421875    },    "861_001_0001_XT": {      "VALUE": 1993.07238769531    },    "DG1": {      "POW": 2006.56140136719    },    "882_001_0429_XI": {      "VALUE": 1903.86511230469    },    "735_001_A101_XI": {      "VALUE": 319.691772460938    },    "735_002_A101_XI": {      "VALUE": 323.857482910156    },    "735_003_A101_XI": {      "VALUE": 312.108032226563    },    "882_002_0429_XI": {      "VALUE": 1986.87414550781    },    "601_001_0001_XI": {      "VALUE": True    },    "601_002_0001_XI": {      "VALUE": True    },    "601_003_0001_XI": {      "VALUE": True    },    "601_004_0001_XI": {      "VALUE": True    }  }] }
json_map = row["messageJsonContent"]


def main():

    a = map(
            lambda x: {**{"timestamp": row["timestampAfterEpochMillis"]}, **x},
            json_map,
        )
    b = list(a)

    print("Unpack dict example")


if __name__ == "__main__":
    main()
