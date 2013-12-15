import atkinsonMacias
import matplotlib.pyplot as plt

def test1():
    '''Recreate figure 20 in paper'''
    R = [20, 30, 40, 50, 75, 100, 150, 200, 250, 300, 350, 400]
    M1 = [7.5] * len(R)
    M2 = [8.0] * len(R)
    M3 = [8.5] * len(R)
    M4 = [9.0] * len(R)

    periods1 = [2]
    periods2 = [0.2]

    spectra11, sigma = atkinsonMacias.spectra(M1, R, periods1)
    spectra12, sigma = atkinsonMacias.spectra(M1, R, periods2)

    spectra21, sigma = atkinsonMacias.spectra(M2, R, periods1)
    spectra22, sigma = atkinsonMacias.spectra(M2, R, periods2)

    spectra31, sigma = atkinsonMacias.spectra(M3, R, periods1)
    spectra32, sigma = atkinsonMacias.spectra(M3, R, periods2)

    spectra41, sigma = atkinsonMacias.spectra(M4, R, periods1)
    spectra42, sigma = atkinsonMacias.spectra(M4, R, periods2)

    plt.subplot(2,2,1)
    plt.loglog(R,spectra11,'--')
    plt.loglog(R,spectra12,'-')
    plt.ylim([1,1200])
    plt.yticks([1, 10,100,1000], [1, 10,100,1000])
    plt.xlim([20,450])
    plt.xticks([20,100,400], [20,100,400])


    plt.subplot(2,2,2)
    plt.loglog(R,spectra21,'--')
    plt.loglog(R,spectra22,'-')
    plt.ylim([1,1200])
    plt.yticks([1, 10,100,1000], [1, 10,100,1000])
    plt.xlim([20,450])
    plt.xticks([20,100,400], [20,100,400])

    plt.subplot(2,2,3)
    plt.loglog(R,spectra31,'--')
    plt.loglog(R,spectra32,'-')
    plt.ylim([1,1200])
    plt.yticks([1, 10,100,1000], [1, 10,100,1000])
    plt.xlim([20,450])
    plt.xticks([20,100,400], [20,100,400])

    plt.subplot(2,2,4)
    plt.loglog(R,spectra41,'--')
    plt.loglog(R,spectra42,'-')
    plt.ylim([1,1200])
    plt.yticks([1, 10,100,1000], [1, 10,100,1000])
    plt.xlim([20,450])
    plt.xticks([20,100,400], [20,100,400])

    plt.show()

if __name__ == '__main__':
    test1()
