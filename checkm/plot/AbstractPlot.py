###############################################################################
#
# AbstractPlot.py - Abstract base class for plotting.
#
###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.transforms as mtransforms

import matplotlib as mpl

import numpy as np

class AbstractPlot(FigureCanvas):
	'''
	Abstract base class for plotting.
	'''
	def __init__(self, options):	
		self.options = options
		
		# Global plot settings
		mpl.rcParams['font.size'] = self.options.font_size
		mpl.rcParams['axes.titlesize'] = self.options.font_size
		mpl.rcParams['axes.labelsize'] = self.options.font_size
		mpl.rcParams['xtick.labelsize'] = self.options.font_size
		mpl.rcParams['ytick.labelsize'] = self.options.font_size
		mpl.rcParams['legend.fontsize'] = self.options.font_size
		
		self.fig = Figure(facecolor='white', dpi=options.dpi)
		
		FigureCanvas.__init__(self, self.fig)

		self.cid = None
		
		self.type = '<none>'
		self.name = '<none>'
		
		self.axesColour = (0.5, 0.5, 0.5)
		
	def savePlot(self, filename, dpi=300):
		imgFormat = filename[filename.rfind('.')+1:len(filename)]
		if imgFormat in ['png', 'pdf', 'ps', 'eps','svg']:			
			self.fig.savefig(filename,format=imgFormat,dpi=dpi,facecolor='white',edgecolor='white')
		else:
			pass

	def labelExtents(self, xLabels, xFontSize, xRotation, yLabels, yFontSize, yRotation):
		self.fig.clear()
		
		tempAxes = self.fig.add_axes([0,0,1.0,1.0])	
		
		tempAxes.set_xticks(np.arange(len(xLabels)))	
		tempAxes.set_yticks(np.arange(len(yLabels)))	
		
		xText = tempAxes.set_xticklabels(xLabels, size=xFontSize, rotation=xRotation)
		yText = tempAxes.set_yticklabels(yLabels, size=yFontSize, rotation=yRotation)
		
		bboxes = []
		for label in xText:
			bbox = label.get_window_extent(self.get_renderer())
			bboxi = bbox.inverse_transformed(self.fig.transFigure)
			bboxes.append(bboxi)
		xLabelBounds = mtransforms.Bbox.union(bboxes)
		
		bboxes = []
		for label in yText:
			bbox = label.get_window_extent(self.get_renderer())
			bboxi = bbox.inverse_transformed(self.fig.transFigure)
			bboxes.append(bboxi)		
		yLabelBounds = mtransforms.Bbox.union(bboxes)			
		
		self.fig.clear()
		
		return xLabelBounds, yLabelBounds
		
	def xLabelExtents(self, labels, fontSize, rotation=0):
		self.fig.clear()
		
		tempAxes = self.fig.add_axes([0,0,1.0,1.0])	
		tempAxes.set_xticks(np.arange(len(labels)))	
		xLabels = tempAxes.set_xticklabels(labels, size=fontSize, rotation=rotation)
		
		bboxes = []
		for label in xLabels:
			bbox = label.get_window_extent(self.get_renderer())
			bboxi = bbox.inverse_transformed(self.fig.transFigure)
			bboxes.append(bboxi)		
		xLabelBounds = mtransforms.Bbox.union(bboxes)		
		
		self.fig.clear()
		
		return xLabelBounds
	
	def yLabelExtents(self, labels, fontSize, rotation=0):
		self.fig.clear()

		tempAxes = self.fig.add_axes([0,0,1.0,1.0])	
		tempAxes.set_yticks(np.arange(len(labels)))	
		yLabels = tempAxes.set_yticklabels(labels, size=fontSize, rotation=rotation)
		
		bboxes = []
		for label in yLabels:
			bbox = label.get_window_extent(self.get_renderer())
			bboxi = bbox.inverse_transformed(self.fig.transFigure)
			bboxes.append(bboxi)		
		yLabelBounds = mtransforms.Bbox.union(bboxes)		
		
		self.fig.clear()
		
		return yLabelBounds

	def formatLabels(self, labels): 
		formattedLabels = []     
		for label in labels: 
			value = float(label.get_text())    
			if value < 0.01:
				valueStr = '%.2e' % value
				if 'e-00' in valueStr:
					valueStr = valueStr.replace('e-00', 'e-')
				elif 'e-0' in valueStr:
					valueStr = valueStr.replace('e-0', 'e-')
			else:
				valueStr = '%.3f' % value
				
			formattedLabels.append(valueStr)
				
		return formattedLabels
	
				