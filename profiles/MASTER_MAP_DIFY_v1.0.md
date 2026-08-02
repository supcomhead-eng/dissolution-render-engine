# MASTER_MAP_DIFY_v1.0

## 1. Purpose

This file is the single source of truth used by the Decision Engine to determine:

- `selected_case_id`
- `selected_case_name`
- `selected_masters`
- `generation_order`
- dependencies between masters
- conditions for generating or skipping each master

The Render Engine must use the exact `master_name` values defined below. File names are case-sensitive and include the `.docx` extension.

---

## 2. Cases

### CASE_001

```yaml
case_id: CASE_001
case_name: HỒ SƠ HẢI QUAN GIẢI THỂ
company_type:
  - TNHH_1TV
  - TNHH_2TV_PLUS
  - CTCP
case_request: hai_quan
description: >
  Bộ hồ sơ đề nghị xác nhận hoàn thành nghĩa vụ nộp thuế đối với hoạt động
  xuất nhập khẩu phục vụ thủ tục giải thể doanh nghiệp.
trigger_conditions:
  all:
    - dissolution_request = true
    - requested_output contains "hai_quan" OR requested_output = "full_dossier"
notes:
  business_notes:
    - Dùng chung cho mọi loại hình doanh nghiệp.
    - Nếu doanh nghiệp chưa phát sinh xuất nhập khẩu, vẫn sinh đủ bộ hồ sơ và ghi nhận "Chưa phát sinh XNK" theo Rulebook.
  required_masters:
    - MASTER_HQ_001
    - MASTER_HQ_002
  optional_masters: []
masters:
  - master_id: MASTER_HQ_001
    master_name: MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx
    generation_order: 1
    document_title: GIẤY GIỚI THIỆU
    document_type: introduction_letter
    required: true
    generate_when:
      all:
        - case_id = CASE_001
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: HAI_QUAN

  - master_id: MASTER_HQ_002
    master_name: HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx
    generation_order: 2
    document_title: CÔNG VĂN ĐỀ NGHỊ XÁC NHẬN HOÀN THÀNH NGHĨA VỤ NỘP THUẾ
    document_type: official_letter
    required: true
    generate_when:
      all:
        - case_id = CASE_001
    depends_on:
      - MASTER_HQ_001
    skip_when: false
    output_group: HAI_QUAN
```

---

### CASE_002

```yaml
case_id: CASE_002
case_name: HỒ SƠ THUẾ GIẢI THỂ
company_type:
  - TNHH_1TV
  - TNHH_2TV_PLUS
  - CTCP
case_request: thue
description: >
  Bộ hồ sơ chấm dứt hiệu lực mã số thuế, cam kết không hoàn thuế,
  xác nhận nghĩa vụ thuế và giấy giới thiệu làm việc với cơ quan thuế.
trigger_conditions:
  all:
    - dissolution_request = true
    - requested_output contains "thue" OR requested_output = "full_dossier"
notes:
  business_notes:
    - Dùng chung cho mọi loại hình doanh nghiệp.
    - Nội dung chủ thể ra quyết định giải thể phải được Render Engine điều chỉnh theo company_type.
  required_masters:
    - MASTER_TAX_001
    - MASTER_TAX_002
    - MASTER_TAX_003
    - MASTER_TAX_004
  optional_masters: []
masters:
  - master_id: MASTER_TAX_001
    master_name: MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx
    generation_order: 1
    document_title: VĂN BẢN ĐỀ NGHỊ CHẤM DỨT HIỆU LỰC MÃ SỐ THUẾ
    document_type: tax_form
    required: true
    generate_when:
      all:
        - case_id = CASE_002
    depends_on: []
    skip_when: false
    output_group: THUE

  - master_id: MASTER_TAX_002
    master_name: MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx
    generation_order: 2
    document_title: CÔNG VĂN CAM KẾT KHÔNG HOÀN THUẾ
    document_type: official_letter
    required: true
    generate_when:
      all:
        - case_id = CASE_002
    depends_on:
      - MASTER_TAX_001
    skip_when: false
    output_group: THUE

  - master_id: MASTER_TAX_003
    master_name: MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx
    generation_order: 3
    document_title: VĂN BẢN ĐỀ NGHỊ XÁC NHẬN VIỆC THỰC HIỆN NGHĨA VỤ THUẾ
    document_type: tax_form
    required: true
    generate_when:
      all:
        - case_id = CASE_002
    depends_on:
      - MASTER_TAX_001
      - MASTER_TAX_002
    skip_when: false
    output_group: THUE

  - master_id: MASTER_TAX_004
    master_name: MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx
    generation_order: 4
    document_title: GIẤY GIỚI THIỆU
    document_type: introduction_letter
    required: true
    generate_when:
      all:
        - case_id = CASE_002
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: THUE
```

---

### CASE_003

```yaml
case_id: CASE_003
case_name: HỒ SƠ SỞ ĐKKD - TNHH MỘT THÀNH VIÊN
company_type:
  - TNHH_1TV
case_request: so_khdt
description: >
  Bộ hồ sơ giải thể tại Cơ quan đăng ký kinh doanh dành cho công ty TNHH một thành viên.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = TNHH_1TV
    - requested_output contains "so_khdt" OR requested_output = "full_dossier"
notes:
  business_notes:
    - Quyết định của chủ sở hữu phải được sinh trước các tài liệu giai đoạn hoàn tất giải thể.
    - Giấy ủy quyền chỉ sinh khi người nộp hồ sơ không phải người đại diện theo pháp luật.
  required_masters:
    - MASTER_1TV_001
    - MASTER_1TV_002
    - MASTER_1TV_003
    - MASTER_1TV_004
  optional_masters:
    - MASTER_1TV_005
masters:
  - master_id: MASTER_1TV_001
    master_name: MASTER_04_QUYET_DINH_GIAI_THE_TNHH_1TV_CLEAN.docx
    generation_order: 1
    document_title: QUYẾT ĐỊNH CỦA CHỦ SỞ HỮU VỀ VIỆC GIẢI THỂ DOANH NGHIỆP
    document_type: decision
    required: true
    generate_when:
      all:
        - case_id = CASE_003
    depends_on: []
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV

  - master_id: MASTER_1TV_002
    master_name: MASTER_05_THONG_BAO_GIAI_THE_SKHDT_CLEAN_V2.docx
    generation_order: 2
    document_title: THÔNG BÁO VỀ VIỆC GIẢI THỂ DOANH NGHIỆP
    document_type: notification
    required: true
    generate_when:
      all:
        - case_id = CASE_003
    depends_on:
      - MASTER_1TV_001
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV

  - master_id: MASTER_1TV_003
    master_name: MASTER_06_BAO_CAO_THANH_LY_TAI_SAN_SKHDT_CLEAN.docx
    generation_order: 3
    document_title: BÁO CÁO THANH LÝ TÀI SẢN DOANH NGHIỆP
    document_type: liquidation_report
    required: true
    generate_when:
      all:
        - case_id = CASE_003
    depends_on:
      - MASTER_1TV_001
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV

  - master_id: MASTER_1TV_004
    master_name: MASTER_05_DANH_SACH_CHU_NO_CLEAN_LANDSCAPE.docx
    generation_order: 4
    document_title: DANH SÁCH CHỦ NỢ VÀ SỐ NỢ ĐÃ THANH TOÁN
    document_type: creditor_list
    required: true
    generate_when:
      all:
        - case_id = CASE_003
    depends_on:
      - MASTER_1TV_001
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV

  - master_id: MASTER_1TV_005
    master_name: MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT.docx
    generation_order: 5
    document_title: GIẤY ỦY QUYỀN
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_003
        - authorized_submission = true
    depends_on:
      - authorized_person_profile
      - MASTER_1TV_001
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_TNHH_1TV
```

---

### CASE_004

```yaml
case_id: CASE_004
case_name: HỒ SƠ SỞ ĐKKD - TNHH HAI THÀNH VIÊN TRỞ LÊN - GIAI ĐOẠN 1
company_type:
  - TNHH_2TV_PLUS
case_request: so_khdt_giai_doan_1
description: >
  Bộ hồ sơ thông qua quyết định giải thể của Hội đồng thành viên.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = TNHH_2TV_PLUS
    - dissolution_stage = 1
notes:
  business_notes:
    - Biên bản họp phải sinh trước quyết định.
    - Phải kiểm tra tổng vốn góp, tỷ lệ góp và tổng số phiếu biểu quyết.
  required_masters:
    - MASTER_2TV_S1_001
    - MASTER_2TV_S1_002
  optional_masters:
    - MASTER_2TV_S1_003
masters:
  - master_id: MASTER_2TV_S1_001
    master_name: MASTER_BIEN_BAN_HOP_HDTV_GIAI_THE_TNHH_2TV_v3_BLOCK_LAP_THANH_VIEN V4.docx
    generation_order: 1
    document_title: BIÊN BẢN HỌP HỘI ĐỒNG THÀNH VIÊN VỀ VIỆC GIẢI THỂ
    document_type: meeting_minutes
    required: true
    generate_when:
      all:
        - case_id = CASE_004
    depends_on:
      - member_list
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD1

  - master_id: MASTER_2TV_S1_002
    master_name: MASTER_04_QUYET_DINH_GIAI_THE_TNHH_2TV_FINAL_v2.docx
    generation_order: 2
    document_title: QUYẾT ĐỊNH HỘI ĐỒNG THÀNH VIÊN VỀ VIỆC GIẢI THỂ
    document_type: decision
    required: true
    generate_when:
      all:
        - case_id = CASE_004
    depends_on:
      - MASTER_2TV_S1_001
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD1

  - master_id: MASTER_2TV_S1_003
    master_name: MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT_FINAL_LOCK v2.docx
    generation_order: 3
    document_title: GIẤY ỦY QUYỀN LẦN 01
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_004
        - authorized_submission = true
    depends_on:
      - MASTER_2TV_S1_001
      - MASTER_2TV_S1_002
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_TNHH_2TV_GD1
```

---

### CASE_005

```yaml
case_id: CASE_005
case_name: HỒ SƠ SỞ ĐKKD - TNHH HAI THÀNH VIÊN TRỞ LÊN - GIAI ĐOẠN 2
company_type:
  - TNHH_2TV_PLUS
case_request: so_khdt_giai_doan_2
description: >
  Bộ hồ sơ hoàn tất giải thể sau khi doanh nghiệp đã thanh lý tài sản và hoàn thành nghĩa vụ.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = TNHH_2TV_PLUS
    - dissolution_stage = 2
    - dissolution_decision_issued = true
notes:
  business_notes:
    - Chỉ sinh sau giai đoạn 1.
    - Báo cáo thanh lý phải phản ánh đầy đủ thành viên và phần vốn được hoàn trả.
  required_masters:
    - MASTER_2TV_S2_001
    - MASTER_2TV_S2_002
    - MASTER_2TV_S2_003
  optional_masters:
    - MASTER_2TV_S2_004
masters:
  - master_id: MASTER_2TV_S2_001
    master_name: MASTER_BAO_CAO_THANH_LY_TAI_SAN_TNHH_2TV_FINAL_LOCK.docx
    generation_order: 1
    document_title: BÁO CÁO THANH LÝ TÀI SẢN DOANH NGHIỆP
    document_type: liquidation_report
    required: true
    generate_when:
      all:
        - case_id = CASE_005
    depends_on:
      - CASE_004
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD2

  - master_id: MASTER_2TV_S2_002
    master_name: MASTER_05_DANH_SACH_CHU_NO_CLEAN_LANDSCAPE.docx
    generation_order: 2
    document_title: DANH SÁCH CHỦ NỢ VÀ SỐ NỢ ĐÃ THANH TOÁN
    document_type: creditor_list
    required: true
    generate_when:
      all:
        - case_id = CASE_005
    depends_on:
      - CASE_004
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD2

  - master_id: MASTER_2TV_S2_003
    master_name: MASTER_05_THONG_BAO_GIAI_THE_SKHDT_CLEAN_V2.docx
    generation_order: 3
    document_title: THÔNG BÁO VỀ VIỆC GIẢI THỂ DOANH NGHIỆP
    document_type: notification
    required: true
    generate_when:
      all:
        - case_id = CASE_005
    depends_on:
      - MASTER_2TV_S2_001
      - MASTER_2TV_S2_002
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD2

  - master_id: MASTER_2TV_S2_004
    master_name: MASTER_GIAY_UY_QUYEN_LAN_02_SKHDT_FINAL_LOCK.docx
    generation_order: 4
    document_title: GIẤY ỦY QUYỀN LẦN 02
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_005
        - authorized_submission = true
    depends_on:
      - MASTER_2TV_S2_001
      - MASTER_2TV_S2_002
      - MASTER_2TV_S2_003
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_TNHH_2TV_GD2
```

---

### CASE_006

```yaml
case_id: CASE_006
case_name: HỒ SƠ SỞ ĐKKD - CÔNG TY CỔ PHẦN - GIAI ĐOẠN 1
company_type:
  - CTCP
case_request: so_khdt_giai_doan_1
description: >
  Bộ hồ sơ thông qua quyết định giải thể của Đại hội đồng cổ đông.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = CTCP
    - dissolution_stage = 1
notes:
  business_notes:
    - Biên bản họp Đại hội đồng cổ đông phải sinh trước quyết định.
    - Phải kiểm tra tổng cổ phần, tỷ lệ sở hữu và tổng phiếu biểu quyết.
  required_masters:
    - MASTER_CTCP_S1_001
    - MASTER_CTCP_S1_002
  optional_masters:
    - MASTER_CTCP_S1_003
masters:
  - master_id: MASTER_CTCP_S1_001
    master_name: MASTER_BIEN_BAN_HOP_DHDCD_GIAI_THE_CTCP_FINAL.docx
    generation_order: 1
    document_title: BIÊN BẢN HỌP ĐẠI HỘI ĐỒNG CỔ ĐÔNG VỀ VIỆC GIẢI THỂ
    document_type: meeting_minutes
    required: true
    generate_when:
      all:
        - case_id = CASE_006
    depends_on:
      - shareholder_list
    skip_when: false
    output_group: SO_KHDT_CTCP_GD1

  - master_id: MASTER_CTCP_S1_002
    master_name: MASTER_01_QUYET_DINH_DHDCD_GIAI_THE_CTCP_V1(1).docx
    generation_order: 2
    document_title: QUYẾT ĐỊNH ĐẠI HỘI ĐỒNG CỔ ĐÔNG VỀ VIỆC GIẢI THỂ
    document_type: decision
    required: true
    generate_when:
      all:
        - case_id = CASE_006
    depends_on:
      - MASTER_CTCP_S1_001
    skip_when: false
    output_group: SO_KHDT_CTCP_GD1

  - master_id: MASTER_CTCP_S1_003
    master_name: MASTER_GIAY_UY_QUYEN_LAN_01_CTCP_CLEAN.docx
    generation_order: 3
    document_title: GIẤY ỦY QUYỀN LẦN 01
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_006
        - authorized_submission = true
    depends_on:
      - MASTER_CTCP_S1_001
      - MASTER_CTCP_S1_002
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_CTCP_GD1
```

---

### CASE_007

```yaml
case_id: CASE_007
case_name: HỒ SƠ SỞ ĐKKD - CÔNG TY CỔ PHẦN - GIAI ĐOẠN 2
company_type:
  - CTCP
case_request: so_khdt_giai_doan_2
description: >
  Bộ hồ sơ hoàn tất giải thể công ty cổ phần sau khi thanh lý và hoàn thành nghĩa vụ.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = CTCP
    - dissolution_stage = 2
    - dissolution_decision_issued = true
notes:
  business_notes:
    - Chỉ sinh sau CASE_006.
    - Báo cáo thanh lý và danh sách chủ nợ phải sinh trước thông báo giải thể lần 02.
  required_masters:
    - MASTER_CTCP_S2_001
    - MASTER_CTCP_S2_002
    - MASTER_CTCP_S2_003
  optional_masters:
    - MASTER_CTCP_S2_004
masters:
  - master_id: MASTER_CTCP_S2_001
    master_name: MASTER_05_BAO_CAO_THANH_LY_TAI_SAN_CTCP_FINAL(3).docx
    generation_order: 1
    document_title: BÁO CÁO THANH LÝ TÀI SẢN DOANH NGHIỆP
    document_type: liquidation_report
    required: true
    generate_when:
      all:
        - case_id = CASE_007
    depends_on:
      - CASE_006
      - shareholder_list
    skip_when: false
    output_group: SO_KHDT_CTCP_GD2

  - master_id: MASTER_CTCP_S2_002
    master_name: MASTER_06_DANH_SACH_CHU_NO_CTCP_CLEAN(2).docx
    generation_order: 2
    document_title: DANH SÁCH CHỦ NỢ VÀ SỐ NỢ ĐÃ THANH TOÁN
    document_type: creditor_list
    required: true
    generate_when:
      all:
        - case_id = CASE_007
    depends_on:
      - CASE_006
    skip_when: false
    output_group: SO_KHDT_CTCP_GD2

  - master_id: MASTER_CTCP_S2_003
    master_name: MASTER_04_THONG_BAO_GIAI_THE_LAN_02_CTCP_CLEAN (1)(1).docx
    generation_order: 3
    document_title: THÔNG BÁO VỀ VIỆC GIẢI THỂ DOANH NGHIỆP
    document_type: notification
    required: true
    generate_when:
      all:
        - case_id = CASE_007
    depends_on:
      - MASTER_CTCP_S2_001
      - MASTER_CTCP_S2_002
    skip_when: false
    output_group: SO_KHDT_CTCP_GD2

  - master_id: MASTER_CTCP_S2_004
    master_name: MASTER_GIAY_UY_QUYEN_LAN_02_CTCP_CLEAN.docx
    generation_order: 4
    document_title: GIẤY ỦY QUYỀN LẦN 02
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_007
        - authorized_submission = true
    depends_on:
      - MASTER_CTCP_S2_001
      - MASTER_CTCP_S2_002
      - MASTER_CTCP_S2_003
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_CTCP_GD2
```

---

### CASE_008

```yaml
case_id: CASE_008
case_name: BỘ HỒ SƠ GIẢI THỂ ĐẦY ĐỦ - TNHH MỘT THÀNH VIÊN
company_type:
  - TNHH_1TV
case_request: full_dossier
description: >
  Bộ hồ sơ đầy đủ gồm Hải quan, Thuế và Sở ĐKKD dành cho công ty TNHH một thành viên.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = TNHH_1TV
    - requested_output = "full_dossier"
notes:
  business_notes:
    - Hải quan và Thuế có thể xử lý song song.
    - Hồ sơ hoàn tất tại Sở ĐKKD chỉ nộp sau khi hoàn thành nghĩa vụ liên quan.
  required_masters:
    - Tất cả master required của CASE_001
    - Tất cả master required của CASE_002
    - Tất cả master required của CASE_003
  optional_masters:
    - MASTER_1TV_005
masters:
  - master_id: MASTER_FULL_1TV_001
    master_name: MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx
    generation_order: 1
    document_title: GIẤY GIỚI THIỆU HẢI QUAN
    document_type: introduction_letter
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: HAI_QUAN
  - master_id: MASTER_FULL_1TV_002
    master_name: HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx
    generation_order: 2
    document_title: CÔNG VĂN XÁC NHẬN NGHĨA VỤ HẢI QUAN
    document_type: official_letter
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - MASTER_FULL_1TV_001
    skip_when: false
    output_group: HAI_QUAN
  - master_id: MASTER_FULL_1TV_003
    master_name: MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx
    generation_order: 3
    document_title: ĐỀ NGHỊ CHẤM DỨT HIỆU LỰC MÃ SỐ THUẾ
    document_type: tax_form
    required: true
    generate_when: case_id = CASE_008
    depends_on: []
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_1TV_004
    master_name: MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx
    generation_order: 4
    document_title: CÔNG VĂN KHÔNG HOÀN THUẾ
    document_type: official_letter
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - MASTER_FULL_1TV_003
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_1TV_005
    master_name: MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx
    generation_order: 5
    document_title: XÁC NHẬN NGHĨA VỤ THUẾ
    document_type: tax_form
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - MASTER_FULL_1TV_003
      - MASTER_FULL_1TV_004
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_1TV_006
    master_name: MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx
    generation_order: 6
    document_title: GIẤY GIỚI THIỆU THUẾ
    document_type: introduction_letter
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_1TV_007
    master_name: MASTER_04_QUYET_DINH_GIAI_THE_TNHH_1TV_CLEAN.docx
    generation_order: 7
    document_title: QUYẾT ĐỊNH CỦA CHỦ SỞ HỮU VỀ VIỆC GIẢI THỂ
    document_type: decision
    required: true
    generate_when: case_id = CASE_008
    depends_on: []
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV
  - master_id: MASTER_FULL_1TV_008
    master_name: MASTER_05_THONG_BAO_GIAI_THE_SKHDT_CLEAN_V2.docx
    generation_order: 8
    document_title: THÔNG BÁO GIẢI THỂ
    document_type: notification
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - MASTER_FULL_1TV_007
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV
  - master_id: MASTER_FULL_1TV_009
    master_name: MASTER_06_BAO_CAO_THANH_LY_TAI_SAN_SKHDT_CLEAN.docx
    generation_order: 9
    document_title: BÁO CÁO THANH LÝ TÀI SẢN
    document_type: liquidation_report
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - MASTER_FULL_1TV_007
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV
  - master_id: MASTER_FULL_1TV_010
    master_name: MASTER_05_DANH_SACH_CHU_NO_CLEAN_LANDSCAPE.docx
    generation_order: 10
    document_title: DANH SÁCH CHỦ NỢ
    document_type: creditor_list
    required: true
    generate_when: case_id = CASE_008
    depends_on:
      - MASTER_FULL_1TV_007
    skip_when: false
    output_group: SO_KHDT_TNHH_1TV
  - master_id: MASTER_FULL_1TV_011
    master_name: MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT.docx
    generation_order: 11
    document_title: GIẤY ỦY QUYỀN
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_008
        - authorized_submission = true
    depends_on:
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_TNHH_1TV
```

---

### CASE_009

```yaml
case_id: CASE_009
case_name: BỘ HỒ SƠ GIẢI THỂ ĐẦY ĐỦ - TNHH HAI THÀNH VIÊN TRỞ LÊN
company_type:
  - TNHH_2TV_PLUS
case_request: full_dossier
description: >
  Bộ hồ sơ đầy đủ gồm Hải quan, Thuế, Sở ĐKKD giai đoạn 1 và giai đoạn 2.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = TNHH_2TV_PLUS
    - requested_output = "full_dossier"
notes:
  business_notes:
    - Giai đoạn 1 phải hoàn thành trước giai đoạn 2.
    - Hải quan và Thuế có thể xử lý song song sau khi có quyết định giải thể.
  required_masters:
    - Tất cả master required của CASE_001
    - Tất cả master required của CASE_002
    - Tất cả master required của CASE_004
    - Tất cả master required của CASE_005
  optional_masters:
    - MASTER_2TV_S1_003
    - MASTER_2TV_S2_004
masters:
  - master_id: MASTER_FULL_2TV_001
    master_name: MASTER_BIEN_BAN_HOP_HDTV_GIAI_THE_TNHH_2TV_v3_BLOCK_LAP_THANH_VIEN V4.docx
    generation_order: 1
    document_title: BIÊN BẢN HỌP HỘI ĐỒNG THÀNH VIÊN
    document_type: meeting_minutes
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - member_list
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD1
  - master_id: MASTER_FULL_2TV_002
    master_name: MASTER_04_QUYET_DINH_GIAI_THE_TNHH_2TV_FINAL_v2.docx
    generation_order: 2
    document_title: QUYẾT ĐỊNH HỘI ĐỒNG THÀNH VIÊN
    document_type: decision
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_001
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD1
  - master_id: MASTER_FULL_2TV_003
    master_name: MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT_FINAL_LOCK v2.docx
    generation_order: 3
    document_title: GIẤY ỦY QUYỀN LẦN 01
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_009
        - authorized_submission = true
    depends_on:
      - MASTER_FULL_2TV_001
      - MASTER_FULL_2TV_002
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_TNHH_2TV_GD1
  - master_id: MASTER_FULL_2TV_004
    master_name: MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx
    generation_order: 4
    document_title: GIẤY GIỚI THIỆU HẢI QUAN
    document_type: introduction_letter
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: HAI_QUAN
  - master_id: MASTER_FULL_2TV_005
    master_name: HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx
    generation_order: 5
    document_title: CÔNG VĂN XÁC NHẬN NGHĨA VỤ HẢI QUAN
    document_type: official_letter
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_004
    skip_when: false
    output_group: HAI_QUAN
  - master_id: MASTER_FULL_2TV_006
    master_name: MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx
    generation_order: 6
    document_title: ĐỀ NGHỊ CHẤM DỨT HIỆU LỰC MÃ SỐ THUẾ
    document_type: tax_form
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_002
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_2TV_007
    master_name: MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx
    generation_order: 7
    document_title: CÔNG VĂN KHÔNG HOÀN THUẾ
    document_type: official_letter
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_006
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_2TV_008
    master_name: MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx
    generation_order: 8
    document_title: XÁC NHẬN NGHĨA VỤ THUẾ
    document_type: tax_form
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_006
      - MASTER_FULL_2TV_007
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_2TV_009
    master_name: MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx
    generation_order: 9
    document_title: GIẤY GIỚI THIỆU THUẾ
    document_type: introduction_letter
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_2TV_010
    master_name: MASTER_BAO_CAO_THANH_LY_TAI_SAN_TNHH_2TV_FINAL_LOCK.docx
    generation_order: 10
    document_title: BÁO CÁO THANH LÝ TÀI SẢN
    document_type: liquidation_report
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_001
      - MASTER_FULL_2TV_002
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD2
  - master_id: MASTER_FULL_2TV_011
    master_name: MASTER_05_DANH_SACH_CHU_NO_CLEAN_LANDSCAPE.docx
    generation_order: 11
    document_title: DANH SÁCH CHỦ NỢ
    document_type: creditor_list
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_002
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD2
  - master_id: MASTER_FULL_2TV_012
    master_name: MASTER_05_THONG_BAO_GIAI_THE_SKHDT_CLEAN_V2.docx
    generation_order: 12
    document_title: THÔNG BÁO GIẢI THỂ
    document_type: notification
    required: true
    generate_when: case_id = CASE_009
    depends_on:
      - MASTER_FULL_2TV_010
      - MASTER_FULL_2TV_011
    skip_when: false
    output_group: SO_KHDT_TNHH_2TV_GD2
  - master_id: MASTER_FULL_2TV_013
    master_name: MASTER_GIAY_UY_QUYEN_LAN_02_SKHDT_FINAL_LOCK.docx
    generation_order: 13
    document_title: GIẤY ỦY QUYỀN LẦN 02
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_009
        - authorized_submission = true
    depends_on:
      - MASTER_FULL_2TV_010
      - MASTER_FULL_2TV_011
      - MASTER_FULL_2TV_012
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_TNHH_2TV_GD2
```

---

### CASE_010

```yaml
case_id: CASE_010
case_name: BỘ HỒ SƠ GIẢI THỂ ĐẦY ĐỦ - CÔNG TY CỔ PHẦN
company_type:
  - CTCP
case_request: full_dossier
description: >
  Bộ hồ sơ đầy đủ gồm Hải quan, Thuế, Sở ĐKKD giai đoạn 1 và giai đoạn 2.
trigger_conditions:
  all:
    - dissolution_request = true
    - company_type = CTCP
    - requested_output = "full_dossier"
notes:
  business_notes:
    - Giai đoạn 1 phải hoàn thành trước giai đoạn 2.
    - Hải quan và Thuế có thể xử lý song song sau khi có quyết định giải thể.
  required_masters:
    - Tất cả master required của CASE_001
    - Tất cả master required của CASE_002
    - Tất cả master required của CASE_006
    - Tất cả master required của CASE_007
  optional_masters:
    - MASTER_CTCP_S1_003
    - MASTER_CTCP_S2_004
masters:
  - master_id: MASTER_FULL_CTCP_001
    master_name: MASTER_BIEN_BAN_HOP_DHDCD_GIAI_THE_CTCP_FINAL.docx
    generation_order: 1
    document_title: BIÊN BẢN HỌP ĐẠI HỘI ĐỒNG CỔ ĐÔNG
    document_type: meeting_minutes
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - shareholder_list
    skip_when: false
    output_group: SO_KHDT_CTCP_GD1
  - master_id: MASTER_FULL_CTCP_002
    master_name: MASTER_01_QUYET_DINH_DHDCD_GIAI_THE_CTCP_V1(1).docx
    generation_order: 2
    document_title: QUYẾT ĐỊNH ĐẠI HỘI ĐỒNG CỔ ĐÔNG
    document_type: decision
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_001
    skip_when: false
    output_group: SO_KHDT_CTCP_GD1
  - master_id: MASTER_FULL_CTCP_003
    master_name: MASTER_GIAY_UY_QUYEN_LAN_01_CTCP_CLEAN.docx
    generation_order: 3
    document_title: GIẤY ỦY QUYỀN LẦN 01
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_010
        - authorized_submission = true
    depends_on:
      - MASTER_FULL_CTCP_001
      - MASTER_FULL_CTCP_002
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_CTCP_GD1
  - master_id: MASTER_FULL_CTCP_004
    master_name: MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx
    generation_order: 4
    document_title: GIẤY GIỚI THIỆU HẢI QUAN
    document_type: introduction_letter
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: HAI_QUAN
  - master_id: MASTER_FULL_CTCP_005
    master_name: HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx
    generation_order: 5
    document_title: CÔNG VĂN XÁC NHẬN NGHĨA VỤ HẢI QUAN
    document_type: official_letter
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_004
    skip_when: false
    output_group: HAI_QUAN
  - master_id: MASTER_FULL_CTCP_006
    master_name: MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx
    generation_order: 6
    document_title: ĐỀ NGHỊ CHẤM DỨT HIỆU LỰC MÃ SỐ THUẾ
    document_type: tax_form
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_002
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_CTCP_007
    master_name: MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx
    generation_order: 7
    document_title: CÔNG VĂN KHÔNG HOÀN THUẾ
    document_type: official_letter
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_006
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_CTCP_008
    master_name: MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx
    generation_order: 8
    document_title: XÁC NHẬN NGHĨA VỤ THUẾ
    document_type: tax_form
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_006
      - MASTER_FULL_CTCP_007
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_CTCP_009
    master_name: MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx
    generation_order: 9
    document_title: GIẤY GIỚI THIỆU THUẾ
    document_type: introduction_letter
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - authorized_person_profile
    skip_when: false
    output_group: THUE
  - master_id: MASTER_FULL_CTCP_010
    master_name: MASTER_05_BAO_CAO_THANH_LY_TAI_SAN_CTCP_FINAL(3).docx
    generation_order: 10
    document_title: BÁO CÁO THANH LÝ TÀI SẢN
    document_type: liquidation_report
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_001
      - MASTER_FULL_CTCP_002
    skip_when: false
    output_group: SO_KHDT_CTCP_GD2
  - master_id: MASTER_FULL_CTCP_011
    master_name: MASTER_06_DANH_SACH_CHU_NO_CTCP_CLEAN(2).docx
    generation_order: 11
    document_title: DANH SÁCH CHỦ NỢ
    document_type: creditor_list
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_002
    skip_when: false
    output_group: SO_KHDT_CTCP_GD2
  - master_id: MASTER_FULL_CTCP_012
    master_name: MASTER_04_THONG_BAO_GIAI_THE_LAN_02_CTCP_CLEAN (1)(1).docx
    generation_order: 12
    document_title: THÔNG BÁO GIẢI THỂ LẦN 02
    document_type: notification
    required: true
    generate_when: case_id = CASE_010
    depends_on:
      - MASTER_FULL_CTCP_010
      - MASTER_FULL_CTCP_011
    skip_when: false
    output_group: SO_KHDT_CTCP_GD2
  - master_id: MASTER_FULL_CTCP_013
    master_name: MASTER_GIAY_UY_QUYEN_LAN_02_CTCP_CLEAN.docx
    generation_order: 13
    document_title: GIẤY ỦY QUYỀN LẦN 02
    document_type: authorization
    required: false
    generate_when:
      all:
        - case_id = CASE_010
        - authorized_submission = true
    depends_on:
      - MASTER_FULL_CTCP_010
      - MASTER_FULL_CTCP_011
      - MASTER_FULL_CTCP_012
      - authorized_person_profile
    skip_when:
      any:
        - authorized_submission = false
        - submitter_is_legal_representative = true
    output_group: SO_KHDT_CTCP_GD2
```

---

## 3. Data Sources

```yaml
data_sources:
  authorized_person_profile:
    source_name: authorized_profiles.json
    source_type: json
    required_when:
      any:
        - document_type = introduction_letter
        - document_type = authorization
    lookup_field: aliases
```

---

## 4. Global Decision Rules

```yaml
decision_rules:
  - rule_id: DR_001
    description: Hải quan và Thuế dùng chung cho mọi loại hình doanh nghiệp.
  - rule_id: DR_002
    description: Chỉ bộ Sở ĐKKD phân loại theo TNHH_1TV, TNHH_2TV_PLUS hoặc CTCP.
  - rule_id: DR_003
    description: Giấy ủy quyền chỉ sinh khi authorized_submission = true và người nộp không phải người đại diện theo pháp luật.
  - rule_id: DR_004
    description: TNHH_2TV_PLUS và CTCP phải sinh biên bản họp trước quyết định.
  - rule_id: DR_005
    description: Hồ sơ giai đoạn 2 chỉ sinh sau khi có quyết định giải thể hợp lệ.
  - rule_id: DR_006
    description: TỔNG SỐ PHIẾU BIỂU QUYẾT của TNHH_2TV_PLUS bằng TỔNG VỐN ĐIỀU LỆ chia 10.000.
  - rule_id: DR_007
    description: Không được tự thay thế master bằng file khác nếu master_name không tồn tại.
```

---

## 5. Validation

```yaml
validation:
  case_rules:
    - rule: Mỗi case phải có ít nhất 1 master.
      severity: error
    - rule: case_id phải duy nhất trong toàn bộ file.
      severity: error
    - rule: case_id không được null hoặc rỗng.
      severity: error
    - rule: case_name không được null hoặc rỗng.
      severity: error
    - rule: company_type không được null hoặc rỗng.
      severity: error
    - rule: trigger_conditions phải tồn tại.
      severity: error

  master_rules:
    - rule: master_id phải duy nhất trong phạm vi toàn bộ file.
      severity: error
    - rule: master_name không được null hoặc rỗng.
      severity: error
    - rule: master_name phải có đuôi .docx.
      severity: error
    - rule: master_name phải tồn tại chính xác trong thư mục masters.
      severity: error
    - rule: Không được chuẩn hóa, đổi chữ hoa/thường, xóa khoảng trắng hoặc sửa hậu tố của master_name.
      severity: error
    - rule: generation_order không được null.
      severity: error
    - rule: generation_order phải là số nguyên dương.
      severity: error
    - rule: generation_order không được trùng trong cùng một case.
      severity: error
    - rule: required chỉ được nhận true hoặc false.
      severity: error
    - rule: generate_when phải tồn tại.
      severity: error
    - rule: depends_on phải là mảng; dùng mảng rỗng nếu không có dependency.
      severity: error
    - rule: skip_when phải tồn tại.
      severity: error
    - rule: output_group không được null hoặc rỗng.
      severity: error

  dependency_rules:
    - rule: Mọi master_id được tham chiếu trong depends_on phải tồn tại trong case hiện tại hoặc là data source/case dependency hợp lệ.
      severity: error
    - rule: Không được có dependency vòng.
      severity: error
    - rule: Master phụ thuộc phải có generation_order nhỏ hơn master đang phụ thuộc, trừ data source và case dependency.
      severity: error

  render_preflight:
    - rule: Chỉ render khi tất cả master required đã được chọn.
      severity: error
    - rule: Dừng render nếu bất kỳ master_name nào không tồn tại.
      severity: error
    - rule: Dừng render nếu còn field bắt buộc chưa có dữ liệu.
      severity: error
    - rule: Dừng render nếu dependency chưa thỏa mãn.
      severity: error
```

---

## 6. Output Contract

```yaml
decision_engine_output:
  required_fields:
    - selected_case_id
    - selected_case_name
    - selected_masters
    - generation_order

  selected_masters_item_schema:
    - master_id
    - master_name
    - generation_order
    - document_title
    - document_type
    - required
    - generate_when
    - depends_on
    - skip_when
    - output_group

  failure_behavior:
    - Không tự đoán master_name.
    - Không tự tạo master mới.
    - Không bỏ qua master required.
    - Trả lỗi validation rõ ràng nếu file master không tồn tại hoặc không đối chiếu được duy nhất.
```
