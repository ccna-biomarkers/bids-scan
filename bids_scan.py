#!/usr/bin/python
from bids import BIDSLayout
from bids.reports import BIDSReport
import numpy as np
import nibabel as nib
import os
import argparse

def bids_report(modality, data, ignore):
        print(data)
        print(ignore)
        layout = BIDSLayout(root=data, ignore=ignore)
        list_bids = layout.get(session=1, datatype=modality, extension='nii.gz')
        institutions = dict()

        all_keys = ['Modality', 'MagneticFieldStrength', 'ImagingFrequency', 'Manufacturer', 'ManufacturersModelName', 'InstitutionName', 'InstitutionalDepartmentName', 'InstitutionAddress', 'DeviceSerialNumber', 'StationName', 'PatientPosition', 'ProcedureStepDescription', 'SoftwareVersions', 'MRAcquisitionType', 'SeriesDescription', 'ProtocolName', 'ScanningSequence', 'SequenceVariant', 'ScanOptions', 'SequenceName', 'ImageType', 'SeriesNumber', 'AcquisitionTime', 'AcquisitionNumber', 'SliceThickness', 'SpacingBetweenSlices', 'SAR', 'EchoTime', 'RepetitionTime', 'FlipAngle', 'PartialFourier', 'BaseResolution', 'ShimSetting', 'TxRefAmp', 'PhaseResolution', 'ReceiveCoilName', 'CoilString', 'PulseSequenceDetails', 'RefLinesPE', 'ConsistencyInfo', 'PercentPhaseFOV', 'EchoTrainLength', 'PhaseEncodingSteps', 'AcquisitionMatrixPE', 'ReconMatrixPE', 'ParallelReductionFactorInPlane', 'PixelBandwidth', 'DwellTime', 'PhaseEncodingDirection', 'SliceTiming', 'ImageOrientationPatientDICOM', 'InPlanePhaseEncodingDirectionDICOM', 'ConversionSoftware', 'ConversionSoftwareVersion', 'Dcm2bidsVersion']

        for bids_file in list_bids:
                print("####")
                niftii_file = bids_file.path
                metadata = bids_file.get_metadata()
                field_strength = "None"
                voxel_size = "None"
                echo_time = "None"
                repetition_time = "None"
                flip_angle = "None"
                if "InstitutionName" in metadata.keys():
                        #print(metadata["InstitutionName"])
                        if (metadata["InstitutionName"] == "IUGM"):
                                print("-----------------------------")
                        if "MagneticFieldStrength" in metadata.keys():
                                field_strength = metadata["MagneticFieldStrength"]
                        if "SpacingBetweenSlices" in metadata.keys():
                                voxel_size = metadata["SpacingBetweenSlices"]
                        if "EchoTime" in metadata.keys():
                                echo_time = metadata["EchoTime"]
                        if "RepetitionTime" in metadata.keys():
                                repetition_time = metadata["RepetitionTime"]
                        if "FlipAngle" in metadata.keys():
                                flip_angle = metadata["FlipAngle"]
                        hdr = nib.load(niftii_file).header
                        n_vol = hdr.get_data_shape()[-1]
                        resolution = str(hdr.get_data_shape()[0]) + "x" + str(hdr.get_data_shape()[0])
                        slice_order = hdr.get_value_label('slice_code')
                        scan_time = (n_vol * float(repetition_time))/60
                        institutions[metadata["InstitutionName"]] = {"field_strength":field_strength, "voxel_size": voxel_size, "resolution": resolution, "echo_time": echo_time, "repetition_time": repetition_time, "flip_angle": flip_angle, "num_vol": n_vol, "matrix_size": resolution, "slice_order": slice_order, "scan_time": scan_time, "filepath": niftii_file}

        title = ".. csv-table:: f-MRI sites parameters\n"
        header = "   :header: \"Site\", \"Field Strength (T)\", \"Voxel size (mm3)\", \"Matrix size\", \"Flip Angle\", \"TE (s)\", \"TR (s)\", \"Volumes\", \"Scan slices order\", \"Scan time (min)\"\n"
        options = "   :widths: 30, 10, 10, 10, 10, 10, 10, 10, 10, 10\n"
        content = ""
        for instit in institutions.keys():
                dic = institutions[instit]
                content += "   \"{}\", {}, {}, {}, {}, {}, {}, {}, \"{}\", {:.2f}\n".format(instit, dic["field_strength"], dic["voxel_size"], dic["matrix_size"], dic["flip_angle"], dic["echo_time"], dic["repetition_time"], dic["num_vol"], dic["slice_order"], dic["scan_time"])

        print(title + header + options + "\n" + content)

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--modality", "-m", type=str, help="modality to report, smust be a bids data type")
        parser.add_argument("--data", "-d", type=str, help="input data path to the bids dataset")
        parser.add_argument("--ignore", "-i", action='append', type=str, help="ignore path to the bids dataset")
        args = parser.parse_args()
        print(args)
        bids_report(**vars(args))
