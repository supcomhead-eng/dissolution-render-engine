# MASTER_MAP_DIFY_v1.0

------------------------------------------------------------------------

# Case: CASE_001

## Case Name

Hồ sơ Hải quan giải thể

## Description

Dùng chung mọi loại hình. Nếu chưa phát sinh XNK, vẫn tạo công văn và
ghi nhận trạng thái chưa phát sinh theo rulebook.

## Company Types

-   ALL

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   MASTER_027 --- Giấy giới thiệu Hải quan --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_001 --- Công văn xác nhận nghĩa vụ hải quan --- Bắt buộc theo
    MASTER_MAP.

## Generation Order

1.  MASTER_027; 2. MASTER_001

## Master Dependencies

-   MASTER_027 phụ thuộc MASTER_035 (DATA_DEPENDENCY) --- Dùng profile
    người được giới thiệu mặc định
-   MASTER_001 phụ thuộc MASTER_027 (SAME_CASE) --- CASE_001

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Dùng chung mọi loại hình. Nếu chưa phát sinh XNK, vẫn tạo công văn và
ghi nhận trạng thái chưa phát sinh theo rulebook.

------------------------------------------------------------------------

# Case: CASE_002

## Case Name

Hồ sơ Thuế giải thể

## Description

Dùng chung mọi loại hình; nội dung lý do/chủ thể phải theo company_type.

## Company Types

-   ALL

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   MASTER_002 --- Đề nghị chấm dứt hiệu lực MST --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_008 --- Công văn không hoàn thuế --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_009 --- Xác nhận không nợ thuế --- Bắt buộc theo MASTER_MAP.
-   MASTER_028 --- Giấy giới thiệu Thuế --- Bắt buộc theo MASTER_MAP.

## Generation Order

1.  MASTER_002; 2. MASTER_008; 3. MASTER_009; 4. MASTER_028

## Master Dependencies

-   MASTER_009 phụ thuộc MASTER_002; MASTER_008 (PROCESS_CONTEXT) ---
    CASE_002
-   MASTER_028 phụ thuộc MASTER_035 (DATA_DEPENDENCY) --- Dùng profile
    người được giới thiệu mặc định

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Dùng chung mọi loại hình; nội dung lý do/chủ thể phải theo company_type.

------------------------------------------------------------------------

# Case: CASE_003

## Case Name

Sở ĐKKD - TNHH 1TV

## Description

Chưa có master ủy quyền TNHH 1TV được khóa riêng; đánh dấu cần xác nhận.

## Company Types

-   TNHH_1TV

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   MASTER_011 --- Quyết định chủ sở hữu TNHH 1TV --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_020 --- Thông báo giải thể Sở ĐKKD --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_021 --- Báo cáo thanh lý TNHH 1TV --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_019 --- Danh sách chủ nợ TNHH --- Bắt buộc theo MASTER_MAP.

## Optional Masters

-   MASTER_030 --- Giấy ủy quyền lần 01 Sở - bản cũ

## Conditional Masters

Nếu authorized_submission = true: thêm MASTER_030 (tạm thời, cần xác
nhận bản chính thức); nếu chủ sở hữu là tổ chức hoặc còn nợ/lao động:
manual review

## Generation Order

1.  MASTER_011; 2. MASTER_020; 3. MASTER_021; 4. MASTER_019; 5.
    MASTER_030 nếu áp dụng

## Master Dependencies

-   MASTER_020 phụ thuộc MASTER_011 hoặc MASTER_013 (PROCESS_DEPENDENCY)
    --- Theo loại hình TNHH
-   MASTER_019 phụ thuộc MASTER_011 hoặc MASTER_013 (CONTENT_DEPENDENCY)
    --- TNHH

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Chưa có master ủy quyền TNHH 1TV được khóa riêng; đánh dấu cần xác nhận.

------------------------------------------------------------------------

# Case: CASE_004

## Case Name

Sở ĐKKD - TNHH 2TV+ giai đoạn 1

## Description

Biên bản tạo trước quyết định để kiểm tra danh sách thành viên, tỷ lệ và
phiếu.

## Company Types

-   TNHH_2TV_PLUS

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   MASTER_026 --- Biên bản họp HĐTV TNHH 2TV+ --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_013 --- Quyết định HĐTV TNHH 2TV+ --- Bắt buộc theo
    MASTER_MAP.

## Optional Masters

-   MASTER_031 --- Giấy ủy quyền lần 01 TNHH 2TV+

## Conditional Masters

Nếu authorized_submission = true: thêm MASTER_031

## Generation Order

1.  MASTER_026; 2. MASTER_013; 3. MASTER_031 nếu áp dụng

## Master Dependencies

-   MASTER_013 phụ thuộc MASTER_026 (CONTENT_DEPENDENCY) ---
    TNHH_2TV_PLUS
-   MASTER_031 phụ thuộc MASTER_013; MASTER_026 (AUTHORIZATION_SCOPE)
    --- authorized_submission = true và TNHH_2TV_PLUS
-   MASTER_031 phụ thuộc MASTER_035 (DATA_DEPENDENCY) --- Nếu dùng
    profile ủy quyền mặc định

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Biên bản tạo trước quyết định để kiểm tra danh sách thành viên, tỷ lệ và
phiếu.

------------------------------------------------------------------------

# Case: CASE_005

## Case Name

Sở ĐKKD - TNHH 2TV+ giai đoạn 2

## Description

Chỉ tạo khi đã có quyết định giải thể và hoàn tất thanh lý/nghĩa vụ.

## Company Types

-   TNHH_2TV_PLUS

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   MASTER_020 --- Thông báo giải thể Sở ĐKKD --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_024 --- Báo cáo thanh lý TNHH 2TV+ --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_019 --- Danh sách chủ nợ TNHH --- Bắt buộc theo MASTER_MAP.

## Optional Masters

-   MASTER_034 --- Giấy ủy quyền lần 02 TNHH 2TV+

## Conditional Masters

Nếu authorized_submission = true: thêm MASTER_034

## Generation Order

1.  MASTER_024; 2. MASTER_019; 3. MASTER_020; 4. MASTER_034 nếu áp dụng

## Master Dependencies

-   MASTER_020 phụ thuộc MASTER_011 hoặc MASTER_013 (PROCESS_DEPENDENCY)
    --- Theo loại hình TNHH
-   MASTER_024 phụ thuộc MASTER_013; MASTER_026 (PROCESS_DEPENDENCY) ---
    Sau quyết định giải thể TNHH 2TV+
-   MASTER_019 phụ thuộc MASTER_011 hoặc MASTER_013 (CONTENT_DEPENDENCY)
    --- TNHH
-   MASTER_034 phụ thuộc MASTER_020; MASTER_024; MASTER_019
    (AUTHORIZATION_SCOPE) --- authorized_submission = true và
    TNHH_2TV_PLUS
-   MASTER_034 phụ thuộc MASTER_035 (DATA_DEPENDENCY) --- Nếu dùng
    profile ủy quyền mặc định

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Chỉ tạo khi đã có quyết định giải thể và hoàn tất thanh lý/nghĩa vụ.

------------------------------------------------------------------------

# Case: CASE_006

## Case Name

Sở ĐKKD - CTCP giai đoạn 1

## Description

Biên bản phải kiểm tra tổng cổ phần, tỷ lệ sở hữu và phiếu trước khi tạo
quyết định.

## Company Types

-   CTCP

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   MASTER_007 --- Biên bản họp ĐHĐCĐ CTCP --- Bắt buộc theo MASTER_MAP.
-   MASTER_003 --- Quyết định giải thể CTCP --- Bắt buộc theo
    MASTER_MAP.

## Optional Masters

-   MASTER_029 --- Giấy ủy quyền lần 01 CTCP

## Conditional Masters

Nếu authorized_submission = true: thêm MASTER_029

## Generation Order

1.  MASTER_007; 2. MASTER_003; 3. MASTER_029 nếu áp dụng

## Master Dependencies

-   MASTER_003 phụ thuộc MASTER_007 (CONTENT_DEPENDENCY) --- CTCP
-   MASTER_029 phụ thuộc MASTER_003; MASTER_007 (AUTHORIZATION_SCOPE)
    --- authorized_submission = true và CTCP
-   MASTER_029 phụ thuộc MASTER_035 (DATA_DEPENDENCY) --- Nếu dùng
    profile ủy quyền mặc định

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Biên bản phải kiểm tra tổng cổ phần, tỷ lệ sở hữu và phiếu trước khi tạo
quyết định.

------------------------------------------------------------------------

# Case: CASE_007

## Case Name

Sở ĐKKD - CTCP giai đoạn 2

## Description

Chỉ tạo khi thanh lý và thanh toán nghĩa vụ đã hoàn tất.

## Company Types

-   CTCP

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   MASTER_018 --- Báo cáo thanh lý tài sản CTCP --- Bắt buộc theo
    MASTER_MAP.
-   MASTER_023 --- Danh sách chủ nợ CTCP --- Bắt buộc theo MASTER_MAP.
-   MASTER_014 --- Thông báo giải thể lần 02 CTCP --- Bắt buộc theo
    MASTER_MAP.

## Optional Masters

-   MASTER_032 --- Giấy ủy quyền lần 02 CTCP

## Conditional Masters

Nếu authorized_submission = true: thêm MASTER_032

## Generation Order

1.  MASTER_018; 2. MASTER_023; 3. MASTER_014; 4. MASTER_032 nếu áp dụng

## Master Dependencies

-   MASTER_018 phụ thuộc MASTER_003; MASTER_007 (PROCESS_DEPENDENCY) ---
    Sau quyết định giải thể CTCP
-   MASTER_023 phụ thuộc MASTER_003 (CONTENT_DEPENDENCY) --- CTCP
-   MASTER_014 phụ thuộc MASTER_003; MASTER_018; MASTER_023
    (PROCESS_DEPENDENCY) --- CTCP giai đoạn 2
-   MASTER_032 phụ thuộc MASTER_014; MASTER_018; MASTER_023
    (AUTHORIZATION_SCOPE) --- authorized_submission = true và CTCP
-   MASTER_032 phụ thuộc MASTER_035 (DATA_DEPENDENCY) --- Nếu dùng
    profile ủy quyền mặc định

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Chỉ tạo khi thanh lý và thanh toán nghĩa vụ đã hoàn tất.

------------------------------------------------------------------------

# Case: CASE_008

## Case Name

Bộ giải thể đầy đủ TNHH 1TV

## Description

Thứ tự nộp thực tế có thể song song giữa Hải quan/Thuế; hồ sơ Sở giai
đoạn cuối phụ thuộc hoàn tất nghĩa vụ.

## Company Types

-   TNHH_1TV

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   CASE_001 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_002 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_003 --- --- Bắt buộc theo MASTER_MAP.

## Generation Order

1.  CASE_001; 2. CASE_002; 3. CASE_003

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Thứ tự nộp thực tế có thể song song giữa Hải quan/Thuế; hồ sơ Sở giai
đoạn cuối phụ thuộc hoàn tất nghĩa vụ.

------------------------------------------------------------------------

# Case: CASE_009

## Case Name

Bộ giải thể đầy đủ TNHH 2TV+

## Description

Giai đoạn 2 chỉ sau khi có quyết định và hoàn tất nghĩa vụ.

## Company Types

-   TNHH_2TV_PLUS

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   CASE_001 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_002 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_004 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_005 --- --- Bắt buộc theo MASTER_MAP.

## Generation Order

1.  CASE_004; 2. CASE_001 và CASE_002; 3. CASE_005

## Master Dependencies

-   CASE_005 phụ thuộc CASE_004 (STAGE_DEPENDENCY) --- TNHH_2TV_PLUS

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Giai đoạn 2 chỉ sau khi có quyết định và hoàn tất nghĩa vụ.

------------------------------------------------------------------------

# Case: CASE_010

## Case Name

Bộ giải thể đầy đủ CTCP

## Description

Giai đoạn 2 chỉ sau khi có quyết định và hoàn tất nghĩa vụ.

## Company Types

-   CTCP

## Required Inputs

-   Company registration certificate (GPKD)
-   Tax code / Enterprise code
-   Legal representative information

## Required Masters

-   CASE_001 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_002 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_006 --- --- Bắt buộc theo MASTER_MAP.
-   CASE_007 --- --- Bắt buộc theo MASTER_MAP.

## Generation Order

1.  CASE_006; 2. CASE_001 và CASE_002; 3. CASE_007

## Master Dependencies

-   CASE_007 phụ thuộc CASE_006 (STAGE_DEPENDENCY) --- CTCP

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name
-   registered_office_address

## Validation

-   Kiểm tra đã chọn đủ master bắt buộc.
-   Nếu thiếu điều kiện xác định case hoặc giai đoạn thì dừng và yêu cầu
    bổ sung.

## Notes

Giai đoạn 2 chỉ sau khi có quyết định và hoàn tất nghĩa vụ.

------------------------------------------------------------------------

# Master: MASTER_001

## Master Name

Công văn xác nhận nghĩa vụ hải quan

## File Name

HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx

## Document Type

Công văn

## Used In Cases

-   CASE_001

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_027 (SAME_CASE)

## Notes

Dùng chung mọi loại hình.

------------------------------------------------------------------------

# Master: MASTER_002

## Master Name

Đề nghị chấm dứt hiệu lực MST

## File Name

MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx

## Document Type

Văn bản đề nghị

## Used In Cases

-   CASE_002

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Dùng chung; nội dung lý do có thể cần điều chỉnh theo loại hình ở bước
render.

------------------------------------------------------------------------

# Master: MASTER_003

## Master Name

Quyết định giải thể CTCP

## File Name

MASTER_01_QUYET_DINH_DHDCD_GIAI_THE_CTCP_V1(1).docx

## Document Type

Quyết định

## Used In Cases

-   CASE_006

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_007 (CONTENT_DEPENDENCY)

## Notes

Bản chính thức đang dùng.

------------------------------------------------------------------------

# Master: MASTER_004

## Master Name

Quyết định giải thể CTCP - bản trùng

## File Name

MASTER_01_QUYET_DINH_DHDCD_GIAI_THE_CTCP_V1.docx

## Document Type

Quyết định

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Không chọn khi MASTER_003 khả dụng.

------------------------------------------------------------------------

# Master: MASTER_005

## Master Name

Biên bản ĐHĐCĐ CTCP - bản cũ 1

## File Name

MASTER_02_BIEN_BAN_HOP_DHDCD_GIAI_THE_CTCP_BLOCK_CO_DONG(1).docx

## Document Type

Biên bản họp

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Được thay bằng MASTER_007.

------------------------------------------------------------------------

# Master: MASTER_006

## Master Name

Biên bản ĐHĐCĐ CTCP - bản cũ 2

## File Name

MASTER_02_BIEN_BAN_HOP_DHDCD_GIAI_THE_CTCP_BLOCK_CO_DONG(2).docx

## Document Type

Biên bản họp

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Được thay bằng MASTER_007.

------------------------------------------------------------------------

# Master: MASTER_007

## Master Name

Biên bản họp ĐHĐCĐ CTCP

## File Name

MASTER_02_BIEN_BAN_HOP_DHDCD_GIAI_THE_CTCP_BLOCK_CO_DONG(3).docx

## Document Type

Biên bản họp

## Used In Cases

-   CASE_006

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Dùng cho giai đoạn thông qua quyết định giải thể.

------------------------------------------------------------------------

# Master: MASTER_008

## Master Name

Công văn không hoàn thuế

## File Name

MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx

## Document Type

Công văn

## Used In Cases

-   CASE_002

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Dùng chung.

------------------------------------------------------------------------

# Master: MASTER_009

## Master Name

Xác nhận không nợ thuế

## File Name

MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx

## Document Type

Mẫu thuế

## Used In Cases

-   CASE_002

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_002; MASTER_008 (PROCESS_CONTEXT)

## Notes

Bản V3 chính thức.

------------------------------------------------------------------------

# Master: MASTER_010

## Master Name

Xác nhận không nợ thuế - bản trùng

## File Name

MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3.docx

## Document Type

Mẫu thuế

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Không chọn khi MASTER_009 khả dụng.

------------------------------------------------------------------------

# Master: MASTER_011

## Master Name

Quyết định chủ sở hữu TNHH 1TV

## File Name

MASTER_04_QUYET_DINH_GIAI_THE_TNHH_1TV_CLEAN (1).docx

## Document Type

Quyết định

## Used In Cases

-   CASE_003

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Bản có hậu tố (1) được coi là bản dùng hiện tại.

------------------------------------------------------------------------

# Master: MASTER_012

## Master Name

Quyết định chủ sở hữu TNHH 1TV - bản trùng

## File Name

MASTER_04_QUYET_DINH_GIAI_THE_TNHH_1TV_CLEAN.docx

## Document Type

Quyết định

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Không chọn khi MASTER_011 khả dụng.

------------------------------------------------------------------------

# Master: MASTER_013

## Master Name

Quyết định HĐTV TNHH 2TV+

## File Name

MASTER_04_QUYET_DINH_GIAI_THE_TNHH_2TV_FINAL_v2.docx

## Document Type

Quyết định

## Used In Cases

-   CASE_004

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_026 (CONTENT_DEPENDENCY)

## Notes

Phụ thuộc biên bản HĐTV.

------------------------------------------------------------------------

# Master: MASTER_014

## Master Name

Thông báo giải thể lần 02 CTCP

## File Name

MASTER_04_THONG_BAO_GIAI_THE_LAN_02_CTCP_CLEAN (1)(1).docx

## Document Type

Thông báo

## Used In Cases

-   CASE_007

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_003; MASTER_018; MASTER_023 (PROCESS_DEPENDENCY)

## Notes

Dùng ở giai đoạn hồ sơ giải thể hoàn tất/lần 02.

------------------------------------------------------------------------

# Master: MASTER_015

## Master Name

Thông báo giải thể CTCP - bản trùng

## File Name

MASTER_04_THONG_BAO_GIAI_THE_LAN_02_CTCP_CLEAN (1).docx

## Document Type

Thông báo

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Không chọn khi MASTER_014 khả dụng.

------------------------------------------------------------------------

# Master: MASTER_016

## Master Name

Báo cáo thanh lý CTCP - bản cũ 1

## File Name

MASTER_05_BAO_CAO_THANH_LY_TAI_SAN_CTCP_FINAL(1).docx

## Document Type

Báo cáo

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Được thay bằng MASTER_018.

------------------------------------------------------------------------

# Master: MASTER_017

## Master Name

Báo cáo thanh lý CTCP - bản cũ 2

## File Name

MASTER_05_BAO_CAO_THANH_LY_TAI_SAN_CTCP_FINAL(2).docx

## Document Type

Báo cáo

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Được thay bằng MASTER_018.

------------------------------------------------------------------------

# Master: MASTER_018

## Master Name

Báo cáo thanh lý tài sản CTCP

## File Name

MASTER_05_BAO_CAO_THANH_LY_TAI_SAN_CTCP_FINAL(3).docx

## Document Type

Báo cáo

## Used In Cases

-   CASE_007

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_003; MASTER_007 (PROCESS_DEPENDENCY)

## Notes

Có block cổ đông ở nhiều vị trí.

------------------------------------------------------------------------

# Master: MASTER_019

## Master Name

Danh sách chủ nợ TNHH

## File Name

MASTER_05_DANH_SACH_CHU_NO_CLEAN_LANDSCAPE.docx

## Document Type

Danh sách

## Used In Cases

-   CASE_003
-   CASE_005

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_011 hoặc MASTER_013 (CONTENT_DEPENDENCY)

## Notes

Dùng cho TNHH 1TV và TNHH 2TV+ theo workflow hiện tại.

------------------------------------------------------------------------

# Master: MASTER_020

## Master Name

Thông báo giải thể Sở ĐKKD

## File Name

MASTER_05_THONG_BAO_GIAI_THE_SKHDT_CLEAN_V2.docx

## Document Type

Thông báo

## Used In Cases

-   CASE_003
-   CASE_005

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_011 hoặc MASTER_013 (PROCESS_DEPENDENCY)

## Notes

Dùng chung TNHH 1TV và TNHH 2TV+; cần xác nhận phân kỳ lần 1/lần 2.

------------------------------------------------------------------------

# Master: MASTER_021

## Master Name

Báo cáo thanh lý TNHH 1TV

## File Name

MASTER_06_BAO_CAO_THANH_LY_TAI_SAN_SKHDT_CLEAN.docx

## Document Type

Báo cáo

## Used In Cases

-   CASE_003

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

------------------------------------------------------------------------

# Master: MASTER_022

## Master Name

Danh sách chủ nợ CTCP - bản cũ

## File Name

MASTER_06_DANH_SACH_CHU_NO_CTCP_CLEAN(1).docx

## Document Type

Danh sách

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Được thay bằng MASTER_023.

------------------------------------------------------------------------

# Master: MASTER_023

## Master Name

Danh sách chủ nợ CTCP

## File Name

MASTER_06_DANH_SACH_CHU_NO_CTCP_CLEAN(2).docx

## Document Type

Danh sách

## Used In Cases

-   CASE_007

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_003 (CONTENT_DEPENDENCY)

## Notes

Mặc định các khoản Không có theo bộ chuẩn.

------------------------------------------------------------------------

# Master: MASTER_024

## Master Name

Báo cáo thanh lý TNHH 2TV+

## File Name

MASTER_BAO_CAO_THANH_LY_TAI_SAN_TNHH_2TV_FINAL_LOCK.docx

## Document Type

Báo cáo

## Used In Cases

-   CASE_005

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_013; MASTER_026 (PROCESS_DEPENDENCY)

------------------------------------------------------------------------

# Master: MASTER_025

## Master Name

Biên bản HĐTV TNHH 2TV+ - bản trùng

## File Name

MASTER_BIEN_BAN_HOP_HDTV_GIAI_THE_TNHH_2TV_v3_BLOCK_LAP_THANH_VIEN
V4(1).docx

## Document Type

Biên bản họp

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Không chọn khi MASTER_026 khả dụng.

------------------------------------------------------------------------

# Master: MASTER_026

## Master Name

Biên bản họp HĐTV TNHH 2TV+

## File Name

MASTER_BIEN_BAN_HOP_HDTV_GIAI_THE_TNHH_2TV_v3_BLOCK_LAP_THANH_VIEN
V4.docx

## Document Type

Biên bản họp

## Used In Cases

-   CASE_004

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Phải tạo trước quyết định để kiểm tra dữ liệu họp.

------------------------------------------------------------------------

# Master: MASTER_027

## Master Name

Giấy giới thiệu Hải quan

## File Name

MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx

## Document Type

Giấy giới thiệu

## Used In Cases

-   CASE_001

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_035 (DATA_DEPENDENCY)

## Notes

Nếu NĐDPL trực tiếp đi nộp có thể cần xác nhận có bỏ hay không.

------------------------------------------------------------------------

# Master: MASTER_028

## Master Name

Giấy giới thiệu Thuế

## File Name

MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx

## Document Type

Giấy giới thiệu

## Used In Cases

-   CASE_002

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_035 (DATA_DEPENDENCY)

## Notes

Theo router hiện tại luôn có.

------------------------------------------------------------------------

# Master: MASTER_029

## Master Name

Giấy ủy quyền lần 01 CTCP

## File Name

MASTER_GIAY_UY_QUYEN_LAN_01_CTCP_CLEAN(1).docx

## Document Type

Giấy ủy quyền

## Used In Cases

-   CASE_006

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_003; MASTER_007 (AUTHORIZATION_SCOPE)
-   MASTER_035 (DATA_DEPENDENCY)

## Notes

Thêm khi người nộp không phải NĐDPL.

------------------------------------------------------------------------

# Master: MASTER_030

## Master Name

Giấy ủy quyền lần 01 Sở - bản cũ

## File Name

MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT.docx

## Document Type

Giấy ủy quyền

## Used In Cases

-   CASE_003

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Được thay bằng MASTER_031 cho TNHH 2TV+; khả năng dùng TNHH 1TV cần xác
nhận.

------------------------------------------------------------------------

# Master: MASTER_031

## Master Name

Giấy ủy quyền lần 01 TNHH 2TV+

## File Name

MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT_FINAL_LOCK v2.docx

## Document Type

Giấy ủy quyền

## Used In Cases

-   CASE_004

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_013; MASTER_026 (AUTHORIZATION_SCOPE)
-   MASTER_035 (DATA_DEPENDENCY)

## Notes

Thêm khi có người được ủy quyền.

------------------------------------------------------------------------

# Master: MASTER_032

## Master Name

Giấy ủy quyền lần 02 CTCP

## File Name

MASTER_GIAY_UY_QUYEN_LAN_02_CTCP_CLEAN(1).docx

## Document Type

Giấy ủy quyền

## Used In Cases

-   CASE_007

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_014; MASTER_018; MASTER_023 (AUTHORIZATION_SCOPE)
-   MASTER_035 (DATA_DEPENDENCY)

## Notes

Thêm khi người nộp không phải NĐDPL.

------------------------------------------------------------------------

# Master: MASTER_033

## Master Name

Giấy ủy quyền lần 02 Sở - bản cũ

## File Name

MASTER_GIAY_UY_QUYEN_LAN_02_SKHDT.docx

## Document Type

Giấy ủy quyền

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Được thay bằng MASTER_034.

------------------------------------------------------------------------

# Master: MASTER_034

## Master Name

Giấy ủy quyền lần 02 TNHH 2TV+

## File Name

MASTER_GIAY_UY_QUYEN_LAN_02_SKHDT_FINAL_LOCK.docx

## Document Type

Giấy ủy quyền

## Used In Cases

-   CASE_005

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Dependencies

-   MASTER_020; MASTER_024; MASTER_019 (AUTHORIZATION_SCOPE)
-   MASTER_035 (DATA_DEPENDENCY)

## Notes

Thêm khi có người được ủy quyền.

------------------------------------------------------------------------

# Master: MASTER_035

## Master Name

Profile người được ủy quyền

## File Name

MASTER_PROFILE_UY_QUYEN_ALIAS (1).docx

## Document Type

Data profile

## Required Canonical Fields

-   company_name
-   enterprise_tax_code
-   legal_representative_name

## Notes

Không phải tài liệu đầu ra; dùng làm nguồn dữ liệu.

# NEEDS_CONFIRMATION

## NC-001 - Master ủy quyền TNHH 1TV

-   **item**: NC-001 - Master ủy quyền TNHH 1TV
-   **reason**: Chưa có file được khóa riêng rõ ràng.
-   **current_understanding**: Tạm hiểu MASTER_030 có thể dùng cho TNHH
    1TV.
-   **recommendation**: Chốt một master riêng hoặc xác nhận MASTER_030
    dùng chung.

## NC-002 - Phân kỳ MASTER_020

-   **item**: NC-002 - Phân kỳ MASTER_020
-   **reason**: Tên file không thể hiện lần 1/lần 2, trong khi TNHH 2TV+
    có ủy quyền hai lần.
-   **current_understanding**: Tạm đặt MASTER_020 ở giai đoạn 2.
-   **recommendation**: Xác nhận thông báo này thuộc giai đoạn nào cho
    TNHH 1TV và TNHH 2TV+.

## NC-003 - Giấy giới thiệu khi NĐDPL trực tiếp nộp

-   **item**: NC-003 - Giấy giới thiệu khi NĐDPL trực tiếp nộp
-   **reason**: Router hiện tại ghi Always, nhưng thực tế có thể không
    cần giới thiệu.
-   **current_understanding**: Tạm coi bắt buộc theo bộ chuẩn.
-   **recommendation**: Xác nhận có được bỏ MASTER_027/028 khi NĐDPL
    trực tiếp làm việc hay không.

## NC-004 - Chủ sở hữu TNHH 1TV là tổ chức

-   **item**: NC-004 - Chủ sở hữu TNHH 1TV là tổ chức
-   **reason**: Master hiện tại có nội dung chủ sở hữu cá nhân.
-   **current_understanding**: Chưa có master riêng cho chủ sở hữu tổ
    chức.
-   **recommendation**: Cần master/rule riêng trước khi tự động hóa.

## NC-005 - Chi nhánh/địa điểm kinh doanh/VPĐD

-   **item**: NC-005 - Chi nhánh/địa điểm kinh doanh/VPĐD
-   **reason**: Hiện không có master chấm dứt đơn vị phụ thuộc trong
    danh sách.
-   **current_understanding**: Không tự thêm file.
-   **recommendation**: Xây master bổ sung khi triển khai case có đơn vị
    phụ thuộc.

## NC-006 - Doanh nghiệp có nợ hoặc lao động

-   **item**: NC-006 - Doanh nghiệp có nợ hoặc lao động
-   **reason**: Các master danh sách chủ nợ và nội dung lao động đang
    mặc định Không có/0.
-   **current_understanding**: Cho phép dùng master nhưng phải thay dữ
    liệu thực tế và manual review.
-   **recommendation**: Cần schema động cho chủ nợ/lao động ở phiên bản
    sau.

## NC-007 - Thứ tự Hải quan và Thuế

-   **item**: NC-007 - Thứ tự Hải quan và Thuế
-   **reason**: Hai luồng có thể thực hiện song song; thứ tự nộp phụ
    thuộc thực tế địa phương.
-   **current_understanding**: MASTER MAP ghi song song trong full
    bundle.
-   **recommendation**: Khi tích hợp workflow, cho phép parallel branch.

## NC-008 - Bản chính thức của các file trùng

-   **item**: NC-008 - Bản chính thức của các file trùng
-   **reason**: Một số master có hậu tố (1), (2), (3) và bản không hậu
    tố.
-   **current_understanding**: Đã chọn bản mới nhất/chốt theo lịch sử
    làm việc.
-   **recommendation**: Nên kiểm tra checksum và khóa kho master trước
    production.

## NC-009 - CTCP có cần cả hai giấy ủy quyền khi cùng một người nộp

-   **item**: NC-009 - CTCP có cần cả hai giấy ủy quyền khi cùng một
    người nộp
-   **reason**: Đã chốt hai master theo hai giai đoạn.
-   **current_understanding**: Tạm thêm theo từng stage nếu
    authorized_submission=true.
-   **recommendation**: Xác nhận có thể dùng một ủy quyền bao trùm cả
    hai giai đoạn hay không.

## NC-010 - Tên cơ quan sau thay đổi tổ chức

-   **item**: NC-010 - Tên cơ quan sau thay đổi tổ chức
-   **reason**: Tên cơ quan ĐKKD/Thuế/Hải quan có thể đổi.
-   **current_understanding**: Không hard-code trong MASTER MAP.
-   **recommendation**: Luôn chạy SEARCH_RULES trước render.
