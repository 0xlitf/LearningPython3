# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smt.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsmt.proto\x12\x15sailyond.smt.protobuf\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\"%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\"&\n\x05Sizef\x12\r\n\x05width\x18\x01 \x01(\x02\x12\x0e\n\x06height\x18\x02 \x01(\x02\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\xa1\x01\n\x04Rect\x12.\n\x08top_left\x18\x01 \x01(\x0b\x32\x1c.sailyond.smt.protobuf.Point\x12\x32\n\x0c\x62ottom_right\x18\x02 \x01(\x0b\x32\x1c.sailyond.smt.protobuf.Point\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x16\n\x0erotation_angle\x18\x05 \x01(\x05\"i\n\x0bRotatedRect\x12,\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x1c.sailyond.smt.protobuf.Point\x12\r\n\x05width\x18\x02 \x01(\x02\x12\x0e\n\x06height\x18\x03 \x01(\x02\x12\r\n\x05\x61ngle\x18\x04 \x01(\x02\"\xa8\x02\n\x05Image\x12\x37\n\x08\x65ncoding\x18\x01 \x01(\x0e\x32%.sailyond.smt.protobuf.Image.Encoding\x12\x37\n\x05\x63olor\x18\x02 \x01(\x0e\x32(.sailyond.smt.protobuf.Image.ColorFormat\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\r\n\x05scale\x18\x05 \x01(\x02\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\"B\n\x08\x45ncoding\x12\x07\n\x03RAW\x10\x00\x12\x08\n\x04JPEG\x10\x01\x12\x07\n\x03PNG\x10\x02\x12\x07\n\x03\x42MP\x10\x03\x12\x08\n\x04WEBP\x10\x04\x12\x07\n\x03URI\x10\x05\"-\n\x0b\x43olorFormat\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05RGB24\x10\x01\x12\t\n\x05\x42GR24\x10\x02\"s\n\x07\x43\x41\x44Info\x12\x10\n\x08panel_id\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\t\x12\x16\n\x0erotation_angle\x18\x03 \x01(\x05\x12,\n\x06\x63\x65nter\x18\x04 \x01(\x0b\x32\x1c.sailyond.smt.protobuf.Point\"h\n\x11\x43\x61\x64PanelAlignInfo\x12\r\n\x05\x61ngle\x18\x01 \x01(\x02\x12\x12\n\nalgo_scale\x18\x02 \x01(\x02\x12\x30\n\ncad_points\x18\x03 \x03(\x0b\x32\x1c.sailyond.smt.protobuf.Point\"\x94\x01\n\x13\x43omponentDetectInfo\x12\x38\n\x0cpackage_type\x18\x01 \x01(\x0e\x32\".sailyond.smt.protobuf.PackageType\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12/\n\x03\x62ox\x18\x03 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\"\x96\x02\n\x0c\x43\x61\x64\x41lignInfo\x12\r\n\x05scale\x18\x01 \x01(\x02\x12\x10\n\x08swap_x_y\x18\x02 \x01(\x08\x12M\n\nalign_info\x18\x03 \x03(\x0b\x32\x39.sailyond.smt.protobuf.CadAlignInfo.CadPanelAlignInfoList\x12?\n\x0b\x64\x65tect_info\x18\x04 \x03(\x0b\x32*.sailyond.smt.protobuf.ComponentDetectInfo\x1aU\n\x15\x43\x61\x64PanelAlignInfoList\x12<\n\nalign_info\x18\x01 \x03(\x0b\x32(.sailyond.smt.protobuf.CadPanelAlignInfo\"n\n\x0fRequiredColumns\x12\x10\n\x08\x63\x65nter_x\x18\x01 \x01(\t\x12\x10\n\x08\x63\x65nter_y\x18\x02 \x01(\t\x12\r\n\x05\x61ngle\x18\x03 \x01(\t\x12\x13\n\x0bposition_id\x18\x04 \x01(\t\x12\x13\n\x0bmaterial_id\x18\x05 \x01(\t\"\x91\x02\n\x07\x43\x41\x44\x44\x61ta\x12\r\n\x05width\x18\x01 \x01(\x04\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x15\n\rpixels_per_mm\x18\x03 \x01(\x02\x12\x15\n\rflip_rotation\x18\x04 \x01(\x08\x12\x12\n\nstart_line\x18\x05 \x01(\x04\x12\x10\n\x08\x65nd_line\x18\x06 \x01(\x04\x12,\n\x04unit\x18\x07 \x01(\x0e\x32\x1e.sailyond.smt.protobuf.CADUnit\x12\x11\n\tcol_order\x18\x08 \x03(\x04\x12\x13\n\x0braw_content\x18\t \x01(\x0c\x12=\n\rrequired_cols\x18\n \x01(\x0b\x32&.sailyond.smt.protobuf.RequiredColumns\"Z\n\x0bModelConfig\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .sailyond.smt.protobuf.ModelType\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\r\n\x05notes\x18\x03 \x01(\t\"^\n\x11\x44\x65\x66\x65\x63tModelConfig\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .sailyond.smt.protobuf.ModelType\x12\x19\n\x11\x64\x65\x66\x65\x63t_model_uuid\x18\x02 \x01(\t\"N\n\x0c\x44\x65\x66\x65\x63tResult\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.sailyond.smt.protobuf.DefectType\x12\r\n\x05score\x18\x02 \x01(\x02\"\xde\x01\n\x10\x44\x65\x66\x65\x63tAlgoResult\x12<\n\x0b\x62inary_type\x18\x01 \x01(\x0e\x32\'.sailyond.smt.protobuf.BinaryDefectType\x12\x34\n\nmodel_type\x18\x02 \x01(\x0e\x32 .sailyond.smt.protobuf.ModelType\x12\x14\n\x0c\x62inary_score\x18\x03 \x01(\x02\x12@\n\x13multi_class_results\x18\x04 \x03(\x0b\x32#.sailyond.smt.protobuf.DefectResult\"\xd5\x01\n\x17\x44\x65\x66\x65\x63tRecommendedResult\x12\x32\n\x07\x64\x65\x66\x65\x63ts\x18\x01 \x03(\x0e\x32!.sailyond.smt.protobuf.DefectType\x12<\n\x0f\x64\x65\x66\x65\x63ts_w_score\x18\x02 \x03(\x0b\x32#.sailyond.smt.protobuf.DefectResult\x12\x0f\n\x07\x63hecked\x18\x0b \x01(\x08\x12\x37\n\x0c\x63hecked_type\x18\x0c \x01(\x0e\x32!.sailyond.smt.protobuf.DefectType\"\xc4\x01\n\x1a\x44\x65\x66\x65\x63tModelThresholdConfig\x12\x34\n\nmodel_type\x18\x01 \x01(\x0e\x32 .sailyond.smt.protobuf.ModelType\x12\x11\n\tthreshold\x18\x02 \x01(\x02\x12\x19\n\x11\x64\x65\x66\x61ult_threshold\x18\x0b \x01(\x02\x12\x1f\n\x17threshold_auto_adjusted\x18\x0c \x01(\x08\x12!\n\x19threshold_auto_adjustment\x18\r \x01(\x02\"\xe7\x02\n\x15\x44\x65\x66\x65\x63tDetectionConfig\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.sailyond.smt.protobuf.DefectType\x12\x11\n\ttolerance\x18\x02 \x01(\x02\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x19\n\x11\x64\x65\x66\x61ult_tolerance\x18\x0b \x01(\x02\x12\x1f\n\x17tolerance_auto_adjusted\x18\x0c \x01(\x08\x12!\n\x19tolerance_auto_adjustment\x18\r \x01(\x02\x12!\n\x19tolerance_manual_adjusted\x18\x0e \x01(\x08\x12#\n\x1btolerance_manual_adjustment\x18\x0f \x01(\x02\x12R\n\x17\x64\x65\x66\x65\x63t_model_thresholds\x18\x15 \x03(\x0b\x32\x31.sailyond.smt.protobuf.DefectModelThresholdConfig\"\xa7\x02\n AlgorithmNormalTemplateMatchArgs\x12\x10\n\x08\x61ngle_lb\x18\x01 \x01(\x02\x12\x10\n\x08\x61ngle_ub\x18\x02 \x01(\x02\x12\x17\n\x0f\x61ngle_step_size\x18\x03 \x01(\x02\x12\x11\n\tn_targets\x18\x04 \x01(\r\x12\x17\n\x0f\x65xtended_margin\x18\x05 \x01(\r\x12\x0f\n\x07n_layer\x18\x06 \x01(\r\x12\x19\n\x11min_template_area\x18\x07 \x01(\r\x12\x11\n\tgrayscale\x18\x08 \x01(\x08\x12<\n\x0cmatch_metric\x18\x15 \x01(\x0e\x32&.sailyond.smt.protobuf.MatchMetricType\x12\x1d\n\x15match_score_threshold\x18\x16 \x01(\x02\"k\n&AlgorithmNormalTemplateMatchThresholds\x12\x13\n\x0bx_threshold\x18\x01 \x01(\x02\x12\x13\n\x0by_threshold\x18\x02 \x01(\x02\x12\x17\n\x0f\x61ngle_threshold\x18\x03 \x01(\x02\"\xac\x02\n$AlgorithmShapeBasedTemplateMatchArgs\x12\x10\n\x08\x61ngle_lb\x18\x01 \x01(\x02\x12\x10\n\x08\x61ngle_ub\x18\x02 \x01(\x02\x12\x17\n\x0f\x61ngle_step_size\x18\x03 \x01(\x02\x12\x11\n\tn_targets\x18\x04 \x01(\r\x12\x17\n\x0f\x65xtended_margin\x18\x05 \x01(\r\x12\x0f\n\x07n_layer\x18\x06 \x01(\r\x12\x19\n\x11min_template_area\x18\x07 \x01(\r\x12\x12\n\nn_features\x18\x15 \x01(\r\x12\x1c\n\x14train_threshold_weak\x18\x16 \x01(\x02\x12\x1e\n\x16train_threshold_strong\x18\x17 \x01(\x02\x12\x1d\n\x15match_score_threshold\x18\x18 \x01(\x02\"o\n*AlgorithmShapeBasedTemplateMatchThresholds\x12\x13\n\x0bx_threshold\x18\x01 \x01(\x02\x12\x13\n\x0by_threshold\x18\x02 \x01(\x02\x12\x17\n\x0f\x61ngle_threshold\x18\x03 \x01(\x02\"\xa9\x02\n\x12\x41lgorithmColorArgs\x12\x17\n\x0fhsv_v_range_min\x18\x01 \x01(\r\x12\x17\n\x0fhsv_v_range_max\x18\x02 \x01(\r\x12$\n\x1chsv_hs_polygon_select_inside\x18\x03 \x01(\x08\x12\x34\n\x0ehsv_hs_polygon\x18\x04 \x03(\x0b\x32\x1c.sailyond.smt.protobuf.Point\x12@\n\x0emask_part_type\x18\x05 \x01(\x0e\x32(.sailyond.smt.protobuf.ComponentPartType\x12\x43\n\x12\x63olor_compare_type\x18\x06 \x01(\x0e\x32\'.sailyond.smt.protobuf.ColorCompareType\"V\n\x18\x41lgorithmColorThresholds\x12\x1c\n\x14masked_threshold_min\x18\x01 \x01(\x02\x12\x1c\n\x14masked_threshold_max\x18\x02 \x01(\x02\"\xad\x01\n\x1b\x41lgorithmSolderShortageArgs\x12\x18\n\x10\x62inary_threshold\x18\x01 \x01(\x02\x12\x16\n\x0eis_white_board\x18\x02 \x01(\x08\x12\x1d\n\x15padding_close_to_body\x18\x03 \x01(\x05\x12\x1e\n\x16padding_away_from_body\x18\x04 \x01(\x05\x12\x1d\n\x15inner_detection_ratio\x18\x05 \x01(\x02\";\n!AlgorithmSolderShortageThresholds\x12\x16\n\x0e\x61rea_threshold\x18\x01 \x01(\x02\"\xdf\x02\n\x14NonDLAlgorithmConfig\x12\x36\n\x0b\x64\x65\x66\x65\x63t_type\x18\x01 \x01(\x0e\x32!.sailyond.smt.protobuf.DefectType\x12<\n\x0e\x61lgorithm_type\x18\x02 \x01(\x0e\x32$.sailyond.smt.protobuf.AlgorithmType\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x34\n\nimage_type\x18\x04 \x01(\x0e\x32 .sailyond.smt.protobuf.ImageType\x12,\n\x0e\x61lgorithm_args\x18\x0b \x01(\x0b\x32\x14.google.protobuf.Any\x12\x32\n\x14\x61lgorithm_thresholds\x18\x0c \x01(\x0b\x32\x14.google.protobuf.Any\x12\x18\n\x0b\x61lgo_result\x18\x15 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_algo_result\"\xd4\x05\n\rComponentPart\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.sailyond.smt.protobuf.ComponentPartType\x12\x30\n\x04rect\x18\x02 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x12\n\nhas_defect\x18\x04 \x01(\x08\x12\x11\n\tparent_id\x18\x03 \x01(\x05\x12\x11\n\tanchor_id\x18\x06 \x01(\x05\x12\x13\n\x0b\x66riends_ids\x18\x05 \x03(\x05\x12\x35\n\talgo_rect\x18\x0b \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x1a\n\x12rect_auto_adjusted\x18\x0c \x01(\x08\x12@\n\x14rect_auto_adjustment\x18\r \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x1b\n\x13rect_manual_created\x18\x0e \x01(\x08\x12\x1c\n\x14rect_manual_adjusted\x18\x0f \x01(\x08\x12\x42\n\x16rect_manual_adjustment\x18\x10 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x18\n\x10\x61nnotation_label\x18\x15 \x01(\t\x12H\n\x13non_dl_algo_configs\x18\x1f \x03(\x0b\x32+.sailyond.smt.protobuf.NonDLAlgorithmConfig\x12\x43\n\x12\x64\x65\x66\x65\x63t_algo_result\x18) \x01(\x0b\x32\'.sailyond.smt.protobuf.DefectAlgoResult\x12M\n\x18\x63ross_check_algo_results\x18* \x03(\x0b\x32+.sailyond.smt.protobuf.CrossCheckAlgoResult\"\x8c\x03\n\x0f\x43omponentDetail\x12\x30\n\x04rect\x18\x01 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x35\n\talgo_rect\x18\x0b \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x1a\n\x12rect_auto_adjusted\x18\x0c \x01(\x08\x12@\n\x14rect_auto_adjustment\x18\r \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x1b\n\x13rect_manual_created\x18\x0e \x01(\x08\x12\x1c\n\x14rect_manual_adjusted\x18\x0f \x01(\x08\x12\x42\n\x16rect_manual_adjustment\x18\x10 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x33\n\x05parts\x18\x15 \x03(\x0b\x32$.sailyond.smt.protobuf.ComponentPart\"\x87\x01\n\x07OCRText\x12\x30\n\x04rect\x18\x01 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x0e\n\x06text_0\x18\x02 \x01(\t\x12\x10\n\x08text_180\x18\x03 \x01(\t\x12\x16\n\x0emodel_text_idx\x18\x04 \x01(\x05\x12\x10\n\x08\x64istance\x18\x05 \x01(\x05\"h\n\x12OCRModelTextConfig\x12\x10\n\x08selected\x18\x01 \x01(\x08\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x1a\n\x12\x63har_err_tolerance\x18\x03 \x01(\r\x12\x16\n\x0emodel_text_idx\x18\x04 \x01(\x05\"|\n\x14\x43rossCheckAlgoResult\x12\x1f\n\x17referenced_component_id\x18\x01 \x01(\x05\x12\x43\n\x12\x64\x65\x66\x65\x63t_algo_result\x18\x02 \x01(\x0b\x32\'.sailyond.smt.protobuf.DefectAlgoResult\"\xef\x07\n\tComponent\x12\x30\n\x08\x63\x61\x64_info\x18\x01 \x01(\x0b\x32\x1e.sailyond.smt.protobuf.CADInfo\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x1b\n\x13\x63heck_parts_enabled\x18\x03 \x01(\x08\x12\x19\n\x11\x63ropped_rgb_image\x18\x0b \x01(\x0c\x12\x1b\n\x13\x63ropped_white_image\x18\x0c \x01(\x0c\x12=\n\x11\x61lgo_package_type\x18\x15 \x01(\x0e\x32\".sailyond.smt.protobuf.PackageType\x12;\n\x13\x61lgo_component_text\x18\x16 \x03(\x0b\x32\x1e.sailyond.smt.protobuf.OCRText\x12\x43\n\x12\x64\x65\x66\x65\x63t_algo_result\x18\x17 \x01(\x0b\x32\'.sailyond.smt.protobuf.DefectAlgoResult\x12M\n\x18\x63ross_check_algo_results\x18\x18 \x03(\x0b\x32+.sailyond.smt.protobuf.CrossCheckAlgoResult\x12J\n\x12recommended_result\x18\x19 \x01(\x0b\x32..sailyond.smt.protobuf.DefectRecommendedResult\x12\x18\n\x10\x61nnotation_label\x18\x1a \x01(\t\x12!\n\x19\x63omponent_text_main_angle\x18\x1b \x01(\x02\x12G\n\x16pad_defect_algo_result\x18\x1c \x01(\x0b\x32\'.sailyond.smt.protobuf.DefectAlgoResult\x12Q\n\x1cpad_cross_check_algo_results\x18\x1d \x03(\x0b\x32+.sailyond.smt.protobuf.CrossCheckAlgoResult\x12\x36\n\x06\x64\x65tail\x18\x1f \x01(\x0b\x32&.sailyond.smt.protobuf.ComponentDetail\x12\x32\n\todb_angle\x18  \x01(\x0e\x32\x1f.sailyond.smt.protobuf.ODBAngle\x12N\n\x18\x64\x65\x66\x65\x63t_detection_configs\x18) \x03(\x0b\x32,.sailyond.smt.protobuf.DefectDetectionConfig\x12Y\n\x1e\x62inary_defect_model_thresholds\x18\x33 \x03(\x0b\x32\x31.sailyond.smt.protobuf.DefectModelThresholdConfig\"\xf9\x10\n\x0e\x43omponentModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x0cpackage_type\x18\x02 \x01(\x0e\x32\".sailyond.smt.protobuf.PackageType\x12\x31\n\x08polarity\x18\x03 \x01(\x0e\x32\x1f.sailyond.smt.protobuf.Polarity\x12\"\n\x1apackage_type_auto_adjusted\x18\x0b \x01(\x08\x12H\n\x1cpackage_type_auto_adjustment\x18\x0c \x01(\x0e\x32\".sailyond.smt.protobuf.PackageType\x12$\n\x1cpackage_type_manual_adjusted\x18\r \x01(\x08\x12J\n\x1epackage_type_manual_adjustment\x18\x0e \x01(\x0e\x32\".sailyond.smt.protobuf.PackageType\x12\x1e\n\x16polarity_auto_adjusted\x18\x15 \x01(\x08\x12\x41\n\x18polarity_auto_adjustment\x18\x16 \x01(\x0e\x32\x1f.sailyond.smt.protobuf.Polarity\x12 \n\x18polarity_manual_adjusted\x18\x17 \x01(\x08\x12\x43\n\x1apolarity_manual_adjustment\x18\x18 \x01(\x0e\x32\x1f.sailyond.smt.protobuf.Polarity\x12(\n polarity_referenced_component_id\x18\x19 \x01(\x05\x12\"\n\x1amisaligned_shift_threshold\x18\x1f \x01(\x02\x12*\n\"default_misaligned_shift_threshold\x18  \x01(\x02\x12\x30\n(misaligned_shift_threshold_auto_adjusted\x18! \x01(\x08\x12\x32\n*misaligned_shift_threshold_auto_adjustment\x18\" \x01(\x02\x12\x32\n*misaligned_shift_threshold_manual_adjusted\x18# \x01(\x08\x12\x34\n,misaligned_shift_threshold_manual_adjustment\x18$ \x01(\x02\x12$\n\x1cmisaligned_shift_y_threshold\x18[ \x01(\x02\x12,\n$default_misaligned_shift_y_threshold\x18\\ \x01(\x02\x12\x32\n*misaligned_shift_y_threshold_auto_adjusted\x18] \x01(\x08\x12\x34\n,misaligned_shift_y_threshold_auto_adjustment\x18^ \x01(\x02\x12\x34\n,misaligned_shift_y_threshold_manual_adjusted\x18_ \x01(\x08\x12\x36\n.misaligned_shift_y_threshold_manual_adjustment\x18` \x01(\x02\x12\"\n\x1amisaligned_angle_threshold\x18) \x01(\x02\x12*\n\"default_misaligned_angle_threshold\x18* \x01(\x02\x12\x30\n(misaligned_angle_threshold_auto_adjusted\x18+ \x01(\x08\x12\x32\n*misaligned_angle_threshold_auto_adjustment\x18, \x01(\x02\x12\x32\n*misaligned_angle_threshold_manual_adjusted\x18- \x01(\x08\x12\x34\n,misaligned_angle_threshold_manual_adjustment\x18. \x01(\x02\x12\x1e\n\x16package_area_threshold\x18\x33 \x01(\x02\x12&\n\x1e\x64\x65\x66\x61ult_package_area_threshold\x18\x34 \x01(\x02\x12,\n$package_area_threshold_auto_adjusted\x18\x35 \x01(\x08\x12.\n&package_area_threshold_auto_adjustment\x18\x36 \x01(\x02\x12.\n&package_area_threshold_manual_adjusted\x18\x37 \x01(\x08\x12\x30\n(package_area_threshold_manual_adjustment\x18\x38 \x01(\x02\x12\x34\n\ncomponents\x18= \x03(\x0b\x32 .sailyond.smt.protobuf.Component\x12#\n\x1bodb_referenced_component_id\x18G \x01(\x05\x12\x13\n\x0bocr_enabled\x18Q \x01(\x08\x12\x19\n\x11ocr_auto_adjusted\x18R \x01(\x08\x12\x1b\n\x13ocr_manual_adjusted\x18S \x01(\x08\x12\x32\n\nalgo_texts\x18T \x03(\x0b\x32\x1e.sailyond.smt.protobuf.OCRText\x12\x43\n\x10ocr_configs_auto\x18U \x03(\x0b\x32).sailyond.smt.protobuf.OCRModelTextConfig\x12\x45\n\x12ocr_configs_manual\x18V \x03(\x0b\x32).sailyond.smt.protobuf.OCRModelTextConfig\x12<\n\x10\x61vg_package_rect\x18\x65 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\"\xb0\x01\n\x07Package\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".sailyond.smt.protobuf.PackageType\x12?\n\x10\x63omponent_models\x18\x33 \x03(\x0b\x32%.sailyond.smt.protobuf.ComponentModel\x12\x32\n\x08outliers\x18= \x03(\x0b\x32 .sailyond.smt.protobuf.Component\"\xe4\x03\n\x11TemplateThumbnail\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x15\n\rtemplate_uuid\x18\x02 \x01(\t\x12\x0b\n\x03rev\x18\x03 \x01(\t\x12\x14\n\x0cproject_name\x18\x04 \x01(\t\x12<\n\x0e\x65\x64iting_status\x18\x05 \x01(\x0e\x32$.sailyond.smt.protobuf.EditingStatus\x12+\n\x05phase\x18\x06 \x01(\x0e\x32\x1c.sailyond.smt.protobuf.Phase\x12\x36\n\x0bupload_mode\x18\x07 \x01(\x0e\x32!.sailyond.smt.protobuf.UploadMode\x12\x36\n\x0b\x64\x65vice_mode\x18\x08 \x01(\x0e\x32!.sailyond.smt.protobuf.DeviceMode\x12\x11\n\tthumbnail\x18\t \x01(\x0c\x12\x39\n\rmodel_configs\x18\x0b \x03(\x0b\x32\".sailyond.smt.protobuf.ModelConfig\x12.\n\ncreated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd1\x03\n\x10TemplateOverview\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x14\n\x0cproject_name\x18\x02 \x01(\t\x12\x10\n\x08pcb_type\x18\x03 \x01(\t\x12\x0b\n\x03\x62om\x18\x04 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x05 \x01(\t\x12*\n\x04size\x18\x06 \x01(\x0b\x32\x1c.sailyond.smt.protobuf.Sizef\x12/\n\npixel_size\x18\x07 \x01(\x0b\x32\x1b.sailyond.smt.protobuf.Size\x12\x0f\n\x07preview\x18\x08 \x01(\x0c\x12\x11\n\tdevice_id\x18\t \x01(\t\x12\x12\n\npanel_rows\x18\x0b \x01(\x05\x12\x12\n\npanel_cols\x18\x0c \x01(\x05\x12\x12\n\nextra_info\x18\x15 \x01(\t\x12\x35\n\x10\x62oard_image_size\x18\x1f \x01(\x0b\x32\x1b.sailyond.smt.protobuf.Size\x12\x38\n\x13original_image_size\x18  \x01(\x0b\x32\x1b.sailyond.smt.protobuf.Size\x12\x36\n\x10selection_roi_tl\x18! \x01(\x0b\x32\x1c.sailyond.smt.protobuf.Point\"\x86\x02\n\tMarkPoint\x12\x11\n\tconfirmed\x18\x01 \x01(\x08\x12\x30\n\x04rect\x18\x0b \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x35\n\talgo_rect\x18\x15 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x1b\n\x13rect_manual_created\x18\x16 \x01(\x08\x12\x1c\n\x14rect_manual_adjusted\x18\x17 \x01(\x08\x12\x42\n\x16rect_manual_adjustment\x18\x18 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\"\xd3\x01\n\x07\x42\x61rcode\x12\x30\n\x04rect\x18\x01 \x01(\x0b\x32\".sailyond.smt.protobuf.RotatedRect\x12\x10\n\x08panel_id\x18\x02 \x01(\x05\x12\x38\n\nrec_status\x18\x0b \x01(\x0e\x32$.sailyond.smt.protobuf.BarcodeStatus\x12\x0c\n\x04text\x18\x0c \x01(\t\x12\x0e\n\x06\x66ormat\x18\r \x01(\t\x12,\n\x06region\x18\x0e \x03(\x0b\x32\x1c.sailyond.smt.protobuf.Point\"\xb6\x01\n\x05Panel\x12\x10\n\x08panel_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x64\x65\x66\x61ult_enabled\x18\x0b \x01(\x08\x12\x1d\n\x15\x65nabled_auto_adjusted\x18\x0c \x01(\x08\x12\x1f\n\x17\x65nabled_auto_adjustment\x18\r \x01(\x08\x12\x1f\n\x17\x65nabled_manual_adjusted\x18\x0e \x01(\x08\x12!\n\x19\x65nabled_manual_adjustment\x18\x0f \x01(\x08\"\xa4\x02\n\x0eTemplateDetail\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x30\n\x08packages\x18\x0b \x03(\x0b\x32\x1e.sailyond.smt.protobuf.Package\x12\x35\n\x0bmark_points\x18\x0c \x03(\x0b\x32 .sailyond.smt.protobuf.MarkPoint\x12;\n\x0e\x63\x61\x64_align_info\x18\r \x01(\x0b\x32#.sailyond.smt.protobuf.CadAlignInfo\x12\x30\n\x08\x62\x61rcodes\x18\x0e \x03(\x0b\x32\x1e.sailyond.smt.protobuf.Barcode\x12,\n\x06panels\x18\x15 \x03(\x0b\x32\x1c.sailyond.smt.protobuf.Panel*J\n\tImageType\x12\x13\n\x0fIMAGE_TYPE_NONE\x10\x00\x12\x14\n\x10IMAGE_TYPE_WHITE\x10\x01\x12\x12\n\x0eIMAGE_TYPE_RGB\x10\x02*D\n\x05Phase\x12\x0e\n\nPHASE_NONE\x10\x00\x12\x15\n\x11PHASE_PROGRAMMING\x10\x01\x12\x14\n\x10PHASE_INSPECTION\x10\x02*@\n\nUploadMode\x12\x14\n\x10UPLOAD_MODE_NONE\x10\x00\x12\x1c\n\x18UPLOAD_MODE_ONLY_DEFECTS\x10\x01*a\n\rEditingStatus\x12\x17\n\x13\x45\x44ITING_STATUS_NONE\x10\x00\x12\x1a\n\x16\x45\x44ITING_STATUS_EDITING\x10\x01\x12\x1b\n\x17\x45\x44ITING_STATUS_FINISHED\x10\x02*G\n\nDeviceMode\x12\x1c\n\x18\x44\x45VICE_MODE_BEFORE_STOVE\x10\x00\x12\x1b\n\x17\x44\x45VICE_MODE_AFTER_STOVE\x10\x01*?\n\x07\x43\x41\x44Unit\x12\x0f\n\x0b\x43\x41\x44_UNIT_MM\x10\x00\x12\x11\n\rCAD_UNIT_INCH\x10\x01\x12\x10\n\x0c\x43\x41\x44_UNIT_MIL\x10\x02*\xe8\x02\n\tModelType\x12\x13\n\x0fMODEL_TYPE_NONE\x10\x00\x12\"\n\x1eMODEL_TYPE_DETECTION_COMPONENT\x10\x01\x12\x1c\n\x18MODEL_TYPE_DETECTION_PAD\x10\x02\x12+\n\'MODEL_TYPE_DETECTION_BODY_AND_SINGLEPIN\x10\x03\x12!\n\x1dMODEL_TYPE_DETECTION_POLARITY\x10\x04\x12\x1e\n\x1aMODEL_TYPE_OCR_COMBINATION\x10\x05\x12\x1f\n\x1bMODEL_TYPE_DEFECT_COMPONENT\x10\x06\x12\x1a\n\x16MODEL_TYPE_DEFECT_BODY\x10\x07\x12\x19\n\x15MODEL_TYPE_DEFECT_PAD\x10\x08\x12\x1c\n\x18MODEL_TYPE_DEFECT_PINPAD\x10\t\x12\x1e\n\x1aMODEL_TYPE_DEFECT_PADGROUP\x10\n*\xb9\x05\n\x0bPackageType\x12\x15\n\x11PACKAGE_TYPE_NONE\x10\x00\x12\x14\n\x10PACKAGE_TYPE_AEC\x10\x01\x12\x15\n\x11PACKAGE_TYPE_CHIP\x10\x02\x12\x14\n\x10PACKAGE_TYPE_MLD\x10\x03\x12\x15\n\x11PACKAGE_TYPE_MELF\x10\x04\x12\x14\n\x10PACKAGE_TYPE_OSC\x10\x05\x12\x14\n\x10PACKAGE_TYPE_BGA\x10\x06\x12\x14\n\x10PACKAGE_TYPE_LCC\x10\x07\x12\x15\n\x11PACKAGE_TYPE_PLCC\x10\x08\x12\x14\n\x10PACKAGE_TYPE_QFP\x10\t\x12\x14\n\x10PACKAGE_TYPE_SOD\x10\n\x12\x14\n\x10PACKAGE_TYPE_SOT\x10\x0b\x12\x15\n\x11PACKAGE_TYPE_SOIC\x10\x0c\x12\x14\n\x10PACKAGE_TYPE_SOJ\x10\r\x12\x14\n\x10PACKAGE_TYPE_SOP\x10\x0e\x12\x14\n\x10PACKAGE_TYPE_SON\x10\x0f\x12\x13\n\x0fPACKAGE_TYPE_TO\x10\x10\x12\x15\n\x11PACKAGE_TYPE_XTAL\x10\x11\x12\x14\n\x10PACKAGE_TYPE_DIP\x10\x12\x12\x1a\n\x16PACKAGE_TYPE_CONNECTOR\x10\x13\x12\x19\n\x15PACKAGE_TYPE_INS_JACK\x10\x14\x12\x19\n\x15PACKAGE_TYPE_LCC_PLCC\x10\x15\x12\x14\n\x10PACKAGE_TYPE_LED\x10\x16\x12\x1a\n\x16PACKAGE_TYPE_PINHEADER\x10\x17\x12\x14\n\x10PACKAGE_TYPE_QFN\x10\x18\x12 \n\x1cPACKAGE_TYPE_RADIO_FREQUENCY\x10\x19\x12\x15\n\x11PACKAGE_TYPE_SLOT\x10\x1a\x12\x18\n\x14PACKAGE_TYPE_UNKNOWN\x10\x63\x12\x16\n\x12\x45XTERNAL_MARKPOINT\x10\x64*^\n\x08Polarity\x12\x11\n\rPOLARITY_NONE\x10\x00\x12\x14\n\x10POLARITY_PRESENT\x10\x01\x12\x13\n\x0fPOLARITY_ABSENT\x10\x02\x12\x14\n\x10POLARITY_UNKNOWN\x10\x03*\xbf\x01\n\rAlgorithmType\x12\x17\n\x13\x41LGORITHM_TYPE_NONE\x10\x00\x12(\n$ALGORITHM_TYPE_NORMAL_TEMPLATE_MATCH\x10\x01\x12-\n)ALGORITHM_TYPE_SHAPE_BASED_TEMPLATE_MATCH\x10\x02\x12\x18\n\x14\x41LGORITHM_TYPE_COLOR\x10\x03\x12\"\n\x1e\x41LGORITHM_TYPE_SOLDER_SHORTAGE\x10\x04*\xe9\x02\n\x11\x43omponentPartType\x12\x1c\n\x18\x43OMPONENT_PART_TYPE_NONE\x10\x00\x12\x1c\n\x18\x43OMPONENT_PART_TYPE_BODY\x10\x01\x12\x1b\n\x17\x43OMPONENT_PART_TYPE_PAD\x10\x02\x12 \n\x1c\x43OMPONENT_PART_TYPE_POLARITY\x10\x03\x12 \n\x1c\x43OMPONENT_PART_TYPE_PADGROUP\x10\x04\x12!\n\x1d\x43OMPONENT_PART_TYPE_SINGLEPIN\x10\x05\x12%\n!COMPONENT_PART_TYPE_DEFECT_REGION\x10\x62\x12\"\n\x1e\x43OMPONENT_PART_TYPE_CUSTOMIZED\x10\x63\x12\"\n\x1e\x43OMPONENT_PART_TYPE_PADWITHPIN\x10\x64\x12%\n!COMPONENT_PART_TYPE_PADWITHOUTPIN\x10\x65*\xe1\x02\n\nDefectType\x12\x14\n\x10\x44\x45\x46\x45\x43T_TYPE_NONE\x10\x00\x12\x17\n\x13\x44\x45\x46\x45\x43T_TYPE_MISSING\x10\x01\x12\x1a\n\x16\x44\x45\x46\x45\x43T_TYPE_MISALIGNED\x10\x02\x12\x15\n\x11\x44\x45\x46\x45\x43T_TYPE_WRONG\x10\x03\x12#\n\x1f\x44\x45\x46\x45\x43T_TYPE_INSUFFICIENT_SOLDER\x10\x04\x12 \n\x1c\x44\x45\x46\x45\x43T_TYPE_EXCESSIVE_SOLDER\x10\x05\x12\x1d\n\x19\x44\x45\x46\x45\x43T_TYPE_PSEUDO_SOLDER\x10\x06\x12\x1f\n\x1b\x44\x45\x46\x45\x43T_TYPE_SOLDER_SHORTAGE\x10\x07\x12\x19\n\x15\x44\x45\x46\x45\x43T_TYPE_TOMBSTONE\x10\x08\x12\x1a\n\x16\x44\x45\x46\x45\x43T_TYPE_OVERTURNED\x10\t\x12\x1b\n\x17\x44\x45\x46\x45\x43T_TYPE_SOLDER_BALL\x10\n\x12\x16\n\x12\x44\x45\x46\x45\x43T_TYPE_OTHERS\x10\x63*e\n\x10\x42inaryDefectType\x12\x1b\n\x17\x42INARY_DEFECT_TYPE_NONE\x10\x00\x12\x19\n\x15\x42INARY_DEFECT_TYPE_OK\x10\x01\x12\x19\n\x15\x42INARY_DEFECT_TYPE_NG\x10\x02*~\n\x0fMatchMetricType\x12\r\n\tTM_SQDIFF\x10\x00\x12\x14\n\x10TM_SQDIFF_NORMED\x10\x01\x12\x0c\n\x08TM_CCORR\x10\x02\x12\x13\n\x0fTM_CCORR_NORMED\x10\x03\x12\r\n\tTM_CCOEFF\x10\x04\x12\x14\n\x10TM_CCOEFF_NORMED\x10\x05*\x8e\x01\n\x10\x43olorCompareType\x12\x1f\n\x1b\x43OLOR_COMPARE_TYPE_ABSOLUTE\x10\x00\x12-\n)COLOR_COMPARE_TYPE_GREATER_THAN_REFERENCE\x10\x01\x12*\n&COLOR_COMPARE_TYPE_LESS_THAN_REFERENCE\x10\x02*g\n\x08ODBAngle\x12\x12\n\x0eODB_ANGLE_NONE\x10\x00\x12\x0f\n\x0bODB_ANGLE_0\x10\x01\x12\x10\n\x0cODB_ANGLE_90\x10\x02\x12\x11\n\rODB_ANGLE_180\x10\x03\x12\x11\n\rODB_ANGLE_270\x10\x04*Q\n\rBarcodeStatus\x12\x11\n\rBARCODE_UNSET\x10\x00\x12\x15\n\x11\x42\x41RCODE_NO_RESULT\x10\x01\x12\x16\n\x12\x42\x41RCODE_RECOGNIZED\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'smt_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGETYPE._serialized_start=11662
  _IMAGETYPE._serialized_end=11736
  _PHASE._serialized_start=11738
  _PHASE._serialized_end=11806
  _UPLOADMODE._serialized_start=11808
  _UPLOADMODE._serialized_end=11872
  _EDITINGSTATUS._serialized_start=11874
  _EDITINGSTATUS._serialized_end=11971
  _DEVICEMODE._serialized_start=11973
  _DEVICEMODE._serialized_end=12044
  _CADUNIT._serialized_start=12046
  _CADUNIT._serialized_end=12109
  _MODELTYPE._serialized_start=12112
  _MODELTYPE._serialized_end=12472
  _PACKAGETYPE._serialized_start=12475
  _PACKAGETYPE._serialized_end=13172
  _POLARITY._serialized_start=13174
  _POLARITY._serialized_end=13268
  _ALGORITHMTYPE._serialized_start=13271
  _ALGORITHMTYPE._serialized_end=13462
  _COMPONENTPARTTYPE._serialized_start=13465
  _COMPONENTPARTTYPE._serialized_end=13826
  _DEFECTTYPE._serialized_start=13829
  _DEFECTTYPE._serialized_end=14182
  _BINARYDEFECTTYPE._serialized_start=14184
  _BINARYDEFECTTYPE._serialized_end=14285
  _MATCHMETRICTYPE._serialized_start=14287
  _MATCHMETRICTYPE._serialized_end=14413
  _COLORCOMPARETYPE._serialized_start=14416
  _COLORCOMPARETYPE._serialized_end=14558
  _ODBANGLE._serialized_start=14560
  _ODBANGLE._serialized_end=14663
  _BARCODESTATUS._serialized_start=14665
  _BARCODESTATUS._serialized_end=14746
  _SIZE._serialized_start=96
  _SIZE._serialized_end=133
  _SIZEF._serialized_start=135
  _SIZEF._serialized_end=173
  _POINT._serialized_start=175
  _POINT._serialized_end=204
  _RECT._serialized_start=207
  _RECT._serialized_end=368
  _ROTATEDRECT._serialized_start=370
  _ROTATEDRECT._serialized_end=475
  _IMAGE._serialized_start=478
  _IMAGE._serialized_end=774
  _IMAGE_ENCODING._serialized_start=661
  _IMAGE_ENCODING._serialized_end=727
  _IMAGE_COLORFORMAT._serialized_start=729
  _IMAGE_COLORFORMAT._serialized_end=774
  _CADINFO._serialized_start=776
  _CADINFO._serialized_end=891
  _CADPANELALIGNINFO._serialized_start=893
  _CADPANELALIGNINFO._serialized_end=997
  _COMPONENTDETECTINFO._serialized_start=1000
  _COMPONENTDETECTINFO._serialized_end=1148
  _CADALIGNINFO._serialized_start=1151
  _CADALIGNINFO._serialized_end=1429
  _CADALIGNINFO_CADPANELALIGNINFOLIST._serialized_start=1344
  _CADALIGNINFO_CADPANELALIGNINFOLIST._serialized_end=1429
  _REQUIREDCOLUMNS._serialized_start=1431
  _REQUIREDCOLUMNS._serialized_end=1541
  _CADDATA._serialized_start=1544
  _CADDATA._serialized_end=1817
  _MODELCONFIG._serialized_start=1819
  _MODELCONFIG._serialized_end=1909
  _DEFECTMODELCONFIG._serialized_start=1911
  _DEFECTMODELCONFIG._serialized_end=2005
  _DEFECTRESULT._serialized_start=2007
  _DEFECTRESULT._serialized_end=2085
  _DEFECTALGORESULT._serialized_start=2088
  _DEFECTALGORESULT._serialized_end=2310
  _DEFECTRECOMMENDEDRESULT._serialized_start=2313
  _DEFECTRECOMMENDEDRESULT._serialized_end=2526
  _DEFECTMODELTHRESHOLDCONFIG._serialized_start=2529
  _DEFECTMODELTHRESHOLDCONFIG._serialized_end=2725
  _DEFECTDETECTIONCONFIG._serialized_start=2728
  _DEFECTDETECTIONCONFIG._serialized_end=3087
  _ALGORITHMNORMALTEMPLATEMATCHARGS._serialized_start=3090
  _ALGORITHMNORMALTEMPLATEMATCHARGS._serialized_end=3385
  _ALGORITHMNORMALTEMPLATEMATCHTHRESHOLDS._serialized_start=3387
  _ALGORITHMNORMALTEMPLATEMATCHTHRESHOLDS._serialized_end=3494
  _ALGORITHMSHAPEBASEDTEMPLATEMATCHARGS._serialized_start=3497
  _ALGORITHMSHAPEBASEDTEMPLATEMATCHARGS._serialized_end=3797
  _ALGORITHMSHAPEBASEDTEMPLATEMATCHTHRESHOLDS._serialized_start=3799
  _ALGORITHMSHAPEBASEDTEMPLATEMATCHTHRESHOLDS._serialized_end=3910
  _ALGORITHMCOLORARGS._serialized_start=3913
  _ALGORITHMCOLORARGS._serialized_end=4210
  _ALGORITHMCOLORTHRESHOLDS._serialized_start=4212
  _ALGORITHMCOLORTHRESHOLDS._serialized_end=4298
  _ALGORITHMSOLDERSHORTAGEARGS._serialized_start=4301
  _ALGORITHMSOLDERSHORTAGEARGS._serialized_end=4474
  _ALGORITHMSOLDERSHORTAGETHRESHOLDS._serialized_start=4476
  _ALGORITHMSOLDERSHORTAGETHRESHOLDS._serialized_end=4535
  _NONDLALGORITHMCONFIG._serialized_start=4538
  _NONDLALGORITHMCONFIG._serialized_end=4889
  _COMPONENTPART._serialized_start=4892
  _COMPONENTPART._serialized_end=5616
  _COMPONENTDETAIL._serialized_start=5619
  _COMPONENTDETAIL._serialized_end=6015
  _OCRTEXT._serialized_start=6018
  _OCRTEXT._serialized_end=6153
  _OCRMODELTEXTCONFIG._serialized_start=6155
  _OCRMODELTEXTCONFIG._serialized_end=6259
  _CROSSCHECKALGORESULT._serialized_start=6261
  _CROSSCHECKALGORESULT._serialized_end=6385
  _COMPONENT._serialized_start=6388
  _COMPONENT._serialized_end=7395
  _COMPONENTMODEL._serialized_start=7398
  _COMPONENTMODEL._serialized_end=9567
  _PACKAGE._serialized_start=9570
  _PACKAGE._serialized_end=9746
  _TEMPLATETHUMBNAIL._serialized_start=9749
  _TEMPLATETHUMBNAIL._serialized_end=10233
  _TEMPLATEOVERVIEW._serialized_start=10236
  _TEMPLATEOVERVIEW._serialized_end=10701
  _MARKPOINT._serialized_start=10704
  _MARKPOINT._serialized_end=10966
  _BARCODE._serialized_start=10969
  _BARCODE._serialized_end=11180
  _PANEL._serialized_start=11183
  _PANEL._serialized_end=11365
  _TEMPLATEDETAIL._serialized_start=11368
  _TEMPLATEDETAIL._serialized_end=11660
# @@protoc_insertion_point(module_scope)
