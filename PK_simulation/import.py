from pandas import *
import GUI
file = GUI.selectFile()
if __name__ == "__main__":
    data = read_csv(file)

    mediaA11 = data["A1A"].tolist()
    mediaA12 = data["A1B"].tolist()

    mediaA21 = data["A2A"].tolist()
    mediaA22 = data["A2B"].tolist()

    mediaA31 = data["A3A"].tolist()
    mediaA32 = data["A3B"].tolist()

    mediaB11 = data["B1A"].tolist()
    mediaB12 = data["B1B"].tolist()

    mediaB21 = data["B2A"].tolist()
    mediaB22 = data["B2B"].tolist()

    mediaB31 = data["B3A"].tolist()
    mediaB32 = data["B3B"].tolist()

