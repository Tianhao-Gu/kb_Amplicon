# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from kb_Amplicon.Utils.MDSUtils import MDSUtils
#END_HEADER


class kb_Amplicon:
    '''
    Module Name:
    kb_Amplicon

    Module Description:
    A KBase module: kb_Amplicon
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.0"
    GIT_URL = "git@github.com:Tianhao-Gu/kb_Amplicon.git"
    GIT_COMMIT_HASH = "013ca538201787b3f13cb29fb368545bf143f0ed"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.config['SDK_CALLBACK_URL'] = self.callback_url
        self.config['KB_AUTH_TOKEN'] = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        self.mds_util = MDSUtils(self.config)
        #END_CONSTRUCTOR
        pass


    def run_metaMDS(self, ctx, params):
        """
        run_metaMDS: perform MDS analysis on an input matrix
        :param params: instance of type "MDSParams" (Input of the run_metaMDS
           function input_obj_ref: object reference to a KBaseMatrices matrix
           workspace_name: name of the workspace mds_matrix_name: name of MDS
           (KBaseExperiments.MDSMatrix) object (output) n_components -
           desired number of n dimensions is chosen for the ordination
           (default 2) metric - Int, if 1, perform metric MDS; otherwise,
           perform nonmetric MDS. (default 0) max_iter - iterations stop once
           a set number of max_iter iterations have occurred (default 300)
           distance_metric - name of the distance the ordination will be
           performed on (Euclidean distance, Manhattan distance (city block
           distance) or Bray distance) default to Bray distance plot_script -
           scripts entered by user for plotting plot_type - type of plot to
           be created (bmp or pdf) plot_name - file name for the plot image
           file) -> structure: parameter "input_obj_ref" of type "obj_ref"
           (An X/Y/Z style reference), parameter "workspace_name" of String,
           parameter "mds_matrix_name" of String, parameter "dimension" of
           String, parameter "n_components" of Long, parameter "metric" of
           Long, parameter "max_iter" of Long, parameter "distance_metric" of
           String, parameter "plot_script" of String, parameter "plot_type"
           of String, parameter "plot_name" of String, parameter
           "attribute_mapping_obj_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "associated_matrix_obj_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "scale_size_by" of
           mapping from String to String, parameter "color_marker_by" of
           mapping from String to String
        :returns: instance of type "MDSOutput" (Ouput of the run_metaMDS
           function mds_ref: object reference (to an object of the MDSMatrix
           data type) report_name: report name generated by KBaseReport
           report_ref: report reference generated by KBaseReport) ->
           structure: parameter "mds_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_metaMDS
        returnVal = self.mds_util.run_metaMDS(params)
        #END run_metaMDS

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_metaMDS return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
