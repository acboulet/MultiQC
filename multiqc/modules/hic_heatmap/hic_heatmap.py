from multiqc.modules.base_module import BaseMultiqcModule
from multiqc.plots import heatmap
import logging

class MultiqcModule(BaseMultiqcModule):
    def __init__(self):
        # Initialise the parent object
        super(MultiqcModule, self).__init__(
          name='My Module',
          anchor='mymod',
          href="http://www.awesome_bioinfo.com/my_module",
          info="is an example analysis module used for writing documentation.",
          doi="01.2345/journal/abc123"
        )

        hmdata = [
                [0.9, 0.87, 0.73, 0.6, 0.2, 0.3],
                [0.87, 1, 0.7, 0.6, 0.9, 0.3],
                [0.73, 0.8, 1, 0.6, 0.9, 0.3],
                [0.6, 0.8, 0.7, 1, 0.9, 0.3],
                [0.2, 0.8, 0.7, 0.6, 1, 0.3],
                [0.3, 0.8, 0.7, 0.6, 0.9, 1],
            ]
        names = [ 'one', 'two', 'three', 'four', 'five', 'six' ]

        self.add_section(
            name="Tester",
            anchor="HiC",
            description="",
            helptext="",
            plot=heatmap.plot(hmdata, names)

        )
  
    hm_html = heatmap.plot(hmdata, names)


    pconfig = {
        'title': None,                 # Plot title - should be in format "Module Name: Plot Title"
        'xTitle': None,                # X-axis title
        'yTitle': None,                # Y-axis title
        'min': None,                   # Minimum value (default: auto)
        'max': None,                   # Maximum value (default: auto)
        'square': True,                # Force the plot to stay square? (Maintain aspect ratio)
        'xcats_samples': True,         # Is the x-axis sample names? Set to False to prevent report toolbox from affecting.
        'ycats_samples': True,         # Is the y-axis sample names? Set to False to prevent report toolbox from affecting.
        'colstops': []                 # Scale colour stops. See below.
        'reverseColors': False,        # Reverse the order of the colour axis
        'decimalPlaces': 2,            # Number of decimal places for tooltip
        'legend': True,                # Colour axis key enabled or not
        'borderWidth': 0,              # Border width between cells
        'datalabels': True,            # Show values in each cell. Defaults True when less than 20 samples.
        'datalabel_colour': '<auto>',  # Colour of text for values. Defaults to auto contrast.
        'height': 512                  # The default height of the interactive plot, in pixels
    }