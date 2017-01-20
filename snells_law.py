from snell_output import SnellOutput

def snellsLaw(heightOfKnownWave, periodOfKnownWave, depthAtKnownLocation, crestAngle, cotanOfNearShoreSlope, depthAtDesiredLocation):
    if heightOfKnownWave < (depthAtKnownLocation * 0.78):
        print "Error: Known wave broken"

    rho = 1.989
    g = 32.17
    m = 1 / cotanOfNearShoreSlope
    return height + period + depth

def main():
    # print(snellsLaw(6, 3, 7, 5, 5, 5))
    temp = SnellOutput()
    temp.yolo()
    print(temp.H0)

main()
