import unittest
from unittest.mock import patch, mock_open
import os
import sys
import seqlen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestSeqLen(unittest.TestCase):
    """Unit tests for seqlen/seqlen.py"""
    def test_get_seqlen_from_json_integer(self):
        """Check a JSON object with seqlen as an integer"""
        json_content_mock_integer = ('{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 3423, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}')
        actual = seqlen.get_seqlen_from_json(json_obj=json_content_mock_integer)
        expected = 3423
        self.assertEqual(expected, actual)

    def test_get_seqlen_from_json_floating(self):
        """Check a JSON object with seqlen as a float"""
        json_content_mock_float = ('{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 34323.432, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}')
        actual = seqlen.get_seqlen_from_json(json_obj=json_content_mock_float)
        expected = 34323.432
        self.assertEqual(expected, actual)

    def test_get_seqlen_from_json_failed(self):
        """Check a JSON object with seqlen as a character"""
        json_content_mock_char = ('{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": GH, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}')
        expected = 'JSON object not valid:'
        with self.assertLogs('seqlen') as log_captured:
            seqlen.get_seqlen_from_json(json_obj=json_content_mock_char)
            self.assertIn(expected, log_captured.output[0])

    def test_get_total_seqlen_from_file_with_integer(self):
        """Check a if seqlen adds up correctly within a file"""
        
        file_content_mock= """{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}"""
        mock_file_path = 'file/path/mock'
        
        with patch('seqlen.open'.format(__name__),
            new=mock_open(read_data=file_content_mock)) as file:
            actual = seqlen.get_total_seqlen_from_file(json_file=mock_file_path)
            file.assert_called_once_with(mock_file_path, encoding='utf-8')
        expected = 6
        self.assertEqual(expected, actual)

    def test_get_total_seqlen_from_file_with_one_line_as_char_log(self):
        """
        Check a if seqlen adds up correctly within a file even if one of the seqlen is wrong
        There is an additional check for the log file output
        """
        
        file_content_mock= """{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}
        {"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "ea", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": ea, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}"""
        mock_file_path = 'file/path/mock'
        expected_log = 'JSON object not valid:'
        expected_num = 5
        with patch('seqlen.open'.format(__name__),
            new=mock_open(read_data=file_content_mock)) as file:
            with self.assertLogs('seqlen') as log_captured:
                actual = seqlen.get_total_seqlen_from_file(json_file=mock_file_path)
                file.assert_called_once_with(mock_file_path, encoding='utf-8')
                self.assertIn(expected_log, log_captured.output[0])
                self.assertEqual(expected_num, actual)
