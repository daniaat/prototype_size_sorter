import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import numpy as np

class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def init_model(self):
        # read image
        time1 = time.time()
        img = cv2.imread(self.IMAGE)
        # convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))
        # save image after operations
        self.IMAGE = img
        # using k-means to cluster pixels
        model = KMeans(n_clusters=self.CLUSTERS).fit(img)
        # the cluster centers are our dominant colors.
        self.COLORS = model.cluster_centers_
        # save labels
        self.LABELS = model.labels_
        self.model = model
        time2 = time.time()
        print((time2 - time1) * 1000.0)
        # returning after converting to integer from float
        # return self.COLORS.astype(int)
        # return self.model

    def output_size(self, frame):
        predicted = self.model.predict(frame)
        dates = np.count_nonzero(predicted==1)
        backgound = np.count_nonzero(predicted==0)
        ### do analysis on what is the percentage  of date in image ###
        size = float(dates/(backgound+dates)) * 100.0
        if size < 20.0:
            return 'small'
        elif size >20.0 and size <40.0:
            return 'meduim'
        else:
            return 'large'


     ### debugging tools, used for visualizaiton image points in 3d space ####
    # def rgb_to_hex(self, rgb):
    #     return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))
    #
    # def plotClusters(self):
    #     # plotting
    #     fig = plt.figure()
    #     ax = Axes3D(fig)
    #     for label, pix in zip(self.LABELS, self.IMAGE):
    #         ax.scatter(pix[0], pix[1], pix[2], color=self.rgb_to_hex(self.COLORS[label]))
    #     plt.show()


