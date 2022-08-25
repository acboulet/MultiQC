#!/usr/bin/env python

""" MultiQC module to parse output from DMA HiCPro matrix files """

from __future__ import print_function
from collections import OrderedDict
import logging
import re

from multiqc import config
from multiqc.plots import heatmap
from multiqc.modules.base_module import BaseMultiqcModule

# Initialize logger
log = logging.getLogger(__name__)

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

        print("did I hit here?")

        # Find all matrix files, and extract data
        self.hic_data = dict()
        for f in self.find_log_files("hic_heatmap"):
            self.parse_matrix_file(f)

        if len(self.hic_data) == 0:
            raise UserWarning

        log.info("Found {} reports".format(len(self.hic_data)))

        # Write parsed report data to a file
        self.write_data_file(self.hic_data, "multiqc_hic_heatmap")

        # self.add_section(
        #     name="Tester",
        #     anchor="HiC",
        #     description="",
        #     helptext="",
        #     plot=heatmap.plot(hmdata, names)

        # )

    def parse_matrix_file(self, f):
        """
        Convert matrix file into a 2-D nested list for heatmap.
        """
        s_name = f["s_name"]

        self.hic_data[s_name] = [[]]
        lines = f["f"].splitlines()
        for l in lines:
            l = l.strip()split("\t")

            # Each line should contain 
            x = int(l[0])
            y = int(l[1])
            value = float(l[2])

            # TODO create a max check of 1000?
            # Check if a new row is needed
            if len(self.hic_data[s_name]) == x:
                self.hic_data[s_name][x - 1].append(value)
            else:
                self.hic_data[s_name].append([])
                self.hic_data[s_name][x - 1].append(value)
            
                



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