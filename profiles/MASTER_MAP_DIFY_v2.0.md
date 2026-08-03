# MASTER_MAP_DIFY_v2.0

## CASE_TNHH_1TV

Case ID: CASE_TNHH_1TV

Company Type: TNHH_1TV

Trigger:
company_type = TNHH_1TV

Keywords:

- công ty TNHH một thành viên
- TNHH 1TV
- giải thể
- hồ sơ giải thể
- full dossier

```yaml
- case_id: CASE_TNHH_1TV
  case_name: Hồ sơ giải thể Công ty TNHH một thành viên
  company_type: TNHH_1TV

  required_masters:
    - master_id: TNHH_1TV_01
      master_name: MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx
      generation_order: 1

    - master_id: TNHH_1TV_02
      master_name: HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx
      generation_order: 2

    - master_id: TNHH_1TV_03
      master_name: MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx
      generation_order: 3

    - master_id: TNHH_1TV_04
      master_name: MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx
      generation_order: 4

    - master_id: TNHH_1TV_05
      master_name: MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx
      generation_order: 5

    - master_id: TNHH_1TV_06
      master_name: MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx
      generation_order: 6

    - master_id: TNHH_1TV_07
      master_name: MASTER_04_QUYET_DINH_GIAI_THE_TNHH_1TV_CLEAN.docx
      generation_order: 7

    - master_id: TNHH_1TV_08
      master_name: MASTER_05_THONG_BAO_GIAI_THE_SKHDT_CLEAN_V2.docx
      generation_order: 8

    - master_id: TNHH_1TV_09
      master_name: MASTER_06_BAO_CAO_THANH_LY_TAI_SAN_SKHDT_CLEAN.docx
      generation_order: 9

    - master_id: TNHH_1TV_10
      master_name: MASTER_05_DANH_SACH_CHU_NO_CLEAN_LANDSCAPE.docx
      generation_order: 10

  conditional_masters:
    - master_id: TNHH_1TV_11
      master_name: MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT.docx
      generation_order: 11
      condition: authorized_submission = true

    - master_id: TNHH_1TV_12
      master_name: MASTER_GIAY_UY_QUYEN_LAN_02_SKHDT.docx
      generation_order: 12
      condition: authorized_submission = true
```

---

## CASE_TNHH_2TV_PLUS

Case ID: CASE_TNHH_2TV_PLUS

Company Type: TNHH_2TV_PLUS

Trigger:
company_type = TNHH_2TV_PLUS

Keywords:

- công ty TNHH hai thành viên trở lên
- TNHH 2TV
- TNHH 2TV+
- giải thể
- hồ sơ giải thể
- full dossier

```yaml
- case_id: CASE_TNHH_2TV_PLUS
  case_name: Hồ sơ giải thể Công ty TNHH hai thành viên trở lên
  company_type: TNHH_2TV_PLUS

  required_masters:
    - master_id: TNHH_2TV_01
      master_name: MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx
      generation_order: 1

    - master_id: TNHH_2TV_02
      master_name: HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx
      generation_order: 2

    - master_id: TNHH_2TV_03
      master_name: MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx
      generation_order: 3

    - master_id: TNHH_2TV_04
      master_name: MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx
      generation_order: 4

    - master_id: TNHH_2TV_05
      master_name: MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx
      generation_order: 5

    - master_id: TNHH_2TV_06
      master_name: MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx
      generation_order: 6

    - master_id: TNHH_2TV_07
      master_name: MASTER_BIEN_BAN_HOP_HDTV_GIAI_THE_TNHH_2TV_v3_BLOCK_LAP_THANH_VIEN V4.docx
      generation_order: 7

    - master_id: TNHH_2TV_08
      master_name: MASTER_04_QUYET_DINH_GIAI_THE_TNHH_2TV_FINAL_v2.docx
      generation_order: 8

    - master_id: TNHH_2TV_09
      master_name: MASTER_BAO_CAO_THANH_LY_TAI_SAN_TNHH_2TV_FINAL_LOCK.docx
      generation_order: 9

    - master_id: TNHH_2TV_10
      master_name: MASTER_05_DANH_SACH_CHU_NO_CLEAN_LANDSCAPE.docx
      generation_order: 10

    - master_id: TNHH_2TV_11
      master_name: MASTER_05_THONG_BAO_GIAI_THE_SKHDT_CLEAN_V2.docx
      generation_order: 11

  conditional_masters:
    - master_id: TNHH_2TV_12
      master_name: MASTER_GIAY_UY_QUYEN_LAN_01_SKHDT_FINAL_LOCK v2.docx
      generation_order: 12
      condition: authorized_submission = true

    - master_id: TNHH_2TV_13
      master_name: MASTER_GIAY_UY_QUYEN_LAN_02_SKHDT_FINAL_LOCK.docx
      generation_order: 13
      condition: authorized_submission = true
```

---

## CASE_CTCP

Case ID: CASE_CTCP

Company Type: CTCP

Trigger:
company_type = CTCP

Keywords:

- công ty cổ phần
- CTCP
- giải thể
- hồ sơ giải thể
- full dossier

```yaml
- case_id: CASE_CTCP
  case_name: Hồ sơ giải thể Công ty cổ phần
  company_type: CTCP

  required_masters:
    - master_id: CTCP_01
      master_name: MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx
      generation_order: 1

    - master_id: CTCP_02
      master_name: HC_02_XAC_NHAN_NGHIA_VU_HAI_QUAN_MASTER_FINAL.docx
      generation_order: 2

    - master_id: CTCP_03
      master_name: MASTER_01_DE_NGHI_DONG_MA_SO_THUE_CLEAN (2).docx
      generation_order: 3

    - master_id: CTCP_04
      master_name: MASTER_02_CONG_VAN_KHONG_HOAN_THUE_CLEAN (3).docx
      generation_order: 4

    - master_id: CTCP_05
      master_name: MASTER_03_XAC_NHAN_KHONG_NO_THUE_LOCK_V3(1).docx
      generation_order: 5

    - master_id: CTCP_06
      master_name: MASTER_GIAY_GIOI_THIEU_THUE_CLEAN (1).docx
      generation_order: 6

    - master_id: CTCP_07
      master_name: MASTER_BIEN_BAN_HOP_DHDCD_GIAI_THE_CTCP_FINAL(2).docx
      generation_order: 7

    - master_id: CTCP_08
      master_name: MASTER_01_QUYET_DINH_DHDCD_GIAI_THE_CTCP_V1(1).docx
      generation_order: 8

    - master_id: CTCP_09
      master_name: MASTER_05_BAO_CAO_THANH_LY_TAI_SAN_CTCP_FINAL(3).docx
      generation_order: 9

    - master_id: CTCP_10
      master_name: MASTER_06_DANH_SACH_CHU_NO_CTCP_CLEAN(2).docx
      generation_order: 10

    - master_id: CTCP_11
      master_name: MASTER_04_THONG_BAO_GIAI_THE_LAN_02_CTCP_CLEAN (1)(1).docx
      generation_order: 11

  conditional_masters:
    - master_id: CTCP_12
      master_name: MASTER_GIAY_UY_QUYEN_LAN_01_CTCP_CLEAN.docx
      generation_order: 12
      condition: authorized_submission = true

    - master_id: CTCP_13
      master_name: MASTER_GIAY_UY_QUYEN_LAN_02_CTCP_CLEAN.docx
      generation_order: 13
      condition: authorized_submission = true
```
