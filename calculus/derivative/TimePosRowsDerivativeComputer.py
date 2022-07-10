import numpy as np


class TimePosRowsDerivativeComputer:
    @staticmethod
    def computer(npTimePosRows:np.array,velCoefficient:float=1)->np.array:
        '''
        This function assumes the first collumn is timestamp
        '''
        timePosVelRows = []
        for counter,npTimePosRow in enumerate(npTimePosRows):
            if counter == 0:
                continue
            elif counter>=1:
                prvTime = npTimePosRows[counter-1][0]
                curTime =  npTimePosRows[counter][0]
                diffTime = curTime-prvTime

                prvPos = npTimePosRows[counter-1][1:]
                curPos = npTimePosRows[counter][1:]
                diffPos = np.subtract(curPos,prvPos)

                curVel = velCoefficient*diffPos/diffTime
                curTimePosVel = np.hstack(np.array([curTime,curPos,curVel],dtype=object))
                timePosVelRows.append(curTimePosVel)
                if counter == 1:
                    timePosVelRows.insert(0,np.hstack(np.array([prvTime,prvPos,curVel],dtype=object)))
        npTimePosVelRows = np.array(timePosVelRows)
        return npTimePosVelRows



if __name__=="__main__":
    npTbArr = np.array(
        [[1.2,3,6,5]
        ,[2.3,9,1,8]
        ,[3.1,7,4,2]
        ,[4.5,5,4,1]]
    )
    npTimePosVelArr = TimePosRowsDerivativeComputer.computer(npTbArr)
    print(npTimePosVelArr)



