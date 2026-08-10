# RULEBOOK_DIFY_v2.0

---

## RULE_RULE_001 — company_name

```yaml
rule_id: RULE_RULE_001
rule_name: company_name
rule_type: RULE
purpose: Ưu tiên nguồn dữ liệu doanh nghiệp
applies_to:
- company_name
trigger: Khi cần điền field company_name.
input_fields:
- GPKD
- CCCD/VNeID
- USER_INPUT
output_field: company_name
processing_logic:
- Đọc tên doanh nghiệp từ GPKD.
- Không lấy tên doanh nghiệp từ CCCD.
- Nếu GPKD mờ/thiếu, yêu cầu người dùng cung cấp lại; không tự đoán.
validation:
- Không rỗng; đối chiếu cùng MST
exceptions: []
```

---

## RULE_RULE_002 — legal_representative_name

```yaml
rule_id: RULE_RULE_002
rule_name: legal_representative_name
rule_type: RULE
purpose: Ưu tiên dữ liệu nhân thân
applies_to:
- legal_representative_name
trigger: Khi cần điền field legal_representative_name.
input_fields:
- GPKD
- CCCD/VNeID
output_field: legal_representative_name
processing_logic:
- Xác định NĐDPL trên GPKD.
- Đối chiếu họ tên với CCCD/VNeID.
- Nếu khác về dữ liệu nhân thân, ưu tiên CCCD/VNeID và ghi log sai khác.
- Không đổi vai trò NĐDPL nếu GPKD không xác nhận.
validation:
- Không rỗng; viết hoa theo master khi cần
exceptions:
- CCCD/VNeID khác GPKD về họ tên/ngày sinh/CCCD
```

---

## RULE_RULE_003 — authorized_person_name

```yaml
rule_id: RULE_RULE_003
rule_name: authorized_person_name
rule_type: RULE
purpose: Lấy hồ sơ người được ủy quyền
applies_to:
- authorized_person_name
trigger: Khi cần điền field authorized_person_name.
input_fields:
- CCCD/VNeID
- profile ủy quyền
- USER_INPUT
output_field: authorized_person_name
processing_logic:
- Ưu tiên profile đã chốt.
- Đối chiếu CCCD/VNeID nếu có.
- Nếu người dùng chọn profile khác, dùng đúng profile được chỉ định.
- Không thay người được ủy quyền bằng người khác.
validation:
- Khớp CCCD
exceptions: []
```

---

## RULE_RULE_004 — document_year

```yaml
rule_id: RULE_RULE_004
rule_name: document_year
rule_type: RULE
purpose: Xác định năm văn bản
applies_to:
- document_year
trigger: Khi cần điền field document_year.
input_fields:
- Ngày hệ thống
- USER_INPUT
output_field: document_year
processing_logic:
- Nếu người dùng chỉ định năm hồ sơ thì dùng năm đó.
- Nếu không, dùng năm hiện hành của hệ thống.
- Không tự điền ngày/tháng nếu master chủ ý để trống.
validation:
- 4 chữ số
- Năm phải là 4 chữ số và nhất quán trong cùng bộ hồ sơ.
exceptions:
- Người dùng yêu cầu ngày ký để trống
```

---

## RULE_RULE_005 — signing_place

```yaml
rule_id: RULE_RULE_005
rule_name: signing_place
rule_type: RULE
purpose: Suy luận nơi ký
applies_to:
- signing_place
trigger: Khi cần điền field signing_place.
input_fields:
- registered_office_address
output_field: signing_place
processing_logic:
- Chuẩn hóa địa giới hiện hành của trụ sở.
- Lấy tỉnh/thành phố trực thuộc trung ương.
- Ghi theo cách dùng trong master, không tự thêm cấp quận/huyện.
validation:
- Phù hợp địa giới hành chính hiện hành
exceptions: []
```

---

## RULE_RULE_006 — person_honorific

```yaml
rule_id: RULE_RULE_006
rule_name: person_honorific
rule_type: RULE
purpose: Suy luận Ông/Bà
applies_to:
- person_honorific
trigger: Khi cần điền field person_honorific.
input_fields:
- person_gender
output_field: person_honorific
processing_logic:
- Xác định đúng chủ thể ngay sau placeholder.
- Nam → Ông.
- Nữ → Bà.
- Không suy từ tên khi thiếu giới tính.
validation:
- Chỉ Ông hoặc Bà
- Không được điền Ông/Bà khi chưa xác định giới tính của đúng chủ thể.
exceptions:
- Thiếu giới tính
```

---

## RULE_RULE_007 — company_abbreviation

```yaml
rule_id: RULE_RULE_007
rule_name: company_abbreviation
rule_type: RULE
purpose: Lấy tên viết tắt
applies_to:
- company_abbreviation
trigger: Khi cần điền field company_abbreviation.
input_fields:
- GPKD
- USER_INPUT
output_field: company_abbreviation
processing_logic:
- Dùng tên viết tắt ghi trên GPKD.
- Nếu không có, yêu cầu người dùng nhập.
- Không tự ghép chữ cái đầu.
validation:
- Không chứa ký tự đường dẫn
exceptions:
- GPKD không có tên viết tắt
```

---

## RULE_RULE_008 — employee_count

```yaml
rule_id: RULE_RULE_008
rule_name: employee_count
rule_type: RULE
purpose: Mặc định số lao động
applies_to:
- employee_count
trigger: Khi cần điền field employee_count.
input_fields:
- Dữ liệu thực tế
- CONSTANT
output_field: employee_count
processing_logic:
- Nếu hồ sơ thực tế có số lao động thì dùng số thực tế.
- Nếu không có dữ liệu và workflow hồ sơ chuẩn áp dụng, dùng 0.
- Không dùng placeholder để trống.
validation:
- Số nguyên \>= 0
exceptions:
- Doanh nghiệp còn lao động hoặc có nghĩa vụ lao động
```

---

## RULE_RULE_009 — share_par_value

```yaml
rule_id: RULE_RULE_009
rule_name: share_par_value
rule_type: RULE
purpose: Mệnh giá cổ phần mặc định
applies_to:
- share_par_value
trigger: Khi cần điền field share_par_value.
input_fields:
- GPKD/danh sách cổ đông
- CONSTANT
output_field: share_par_value
processing_logic:
- Nếu hồ sơ ghi mệnh giá thì dùng giá trị hồ sơ.
- Nếu không ghi, mặc định 10.000 đồng/cổ phần.
validation:
- 10.000, trừ khi giấy tờ thể hiện khác
exceptions: []
```

---

## RULE_RULE_010 — shareholder_share_value

```yaml
rule_id: RULE_RULE_010
rule_name: shareholder_share_value
rule_type: RULE
purpose: Tính giá trị cổ phần
applies_to:
- shareholder_share_value
trigger: Khi cần điền field shareholder_share_value.
input_fields:
- shareholder_share_count
- share_par_value
output_field: shareholder_share_value
processing_logic:
- Nhân số cổ phần với mệnh giá; làm tròn về số nguyên đồng; định dạng dấu chấm phân tách nghìn.
validation:
- Khớp tỷ lệ và tổng giá trị
exceptions:
- Giá trị hoàn trả từng cổ đông khác giá trị cổ phần
```

---

## RULE_RULE_011 — shareholder_vote_count

```yaml
rule_id: RULE_RULE_011
rule_name: shareholder_vote_count
rule_type: RULE
purpose: Tính phiếu biểu quyết cổ đông
applies_to:
- shareholder_vote_count
trigger: Khi cần điền field shareholder_vote_count.
input_fields:
- shareholder_share_count
- shareholder_share_type
output_field: shareholder_vote_count
processing_logic:
- Nếu loại cổ phần là Phổ thông thì số phiếu bằng số cổ phần. Nếu loại khác, không tự tính và chuyển NEEDS_CONFIRMATION.
validation:
- Số nguyên \>= 0
exceptions: []
```

---

## RULE_RULE_012 — total_votes_present

```yaml
rule_id: RULE_RULE_012
rule_name: total_votes_present
rule_type: RULE
purpose: Tổng phiếu dự họp CTCP
applies_to:
- total_votes_present
trigger: Khi cần điền field total_votes_present.
input_fields:
- shareholder_vote_count của cổ đông dự họp
output_field: total_votes_present
processing_logic:
- Cộng số phiếu của tất cả cổ đông được đánh dấu có mặt/được tính quyền biểu quyết. Workflow hiện tại mặc định toàn bộ cổ đông có mặt và đạt 100%.
validation:
- Số nguyên; khớp tổng cổ phần dự họp
- Tổng phiếu phải bằng tổng phiếu của cổ đông dự họp.
exceptions: []
```

---

## RULE_RULE_013 — total_voting_ballots_tnhh

```yaml
rule_id: RULE_RULE_013
rule_name: total_voting_ballots_tnhh
rule_type: RULE
purpose: Tổng phiếu biểu quyết TNHH
applies_to:
- total_voting_ballots_tnhh
trigger: Khi cần điền field total_voting_ballots_tnhh.
input_fields:
- charter_capital_amount
output_field: total_voting_ballots_tnhh
processing_logic:
- Chia tổng vốn điều lệ cho 10.000; kết quả phải là số nguyên; định dạng phân tách nghìn.
validation: []
exceptions: []
```

---

## RULE_RULE_014 — member_capital_ratio

```yaml
rule_id: RULE_RULE_014
rule_name: member_capital_ratio
rule_type: RULE
purpose: Tỷ lệ góp vốn
applies_to:
- member_capital_ratio
trigger: Khi cần điền field member_capital_ratio.
input_fields:
- member_capital_amount
- charter_capital_amount
- GPKD
output_field: member_capital_ratio
processing_logic:
- Ưu tiên tỷ lệ trên GPKD. Nếu thiếu, tính vốn góp/tổng vốn × 100. Tổng các thành viên phải bằng 100%.
validation:
- 0--100%; tổng danh sách = 100%
- Tổng tỷ lệ góp vốn của toàn bộ thành viên = 100%.
exceptions:
- Master không có ký hiệu % ngoài placeholder
```

---

## RULE_RULE_015 — shareholder_ownership_percentage

```yaml
rule_id: RULE_RULE_015
rule_name: shareholder_ownership_percentage
rule_type: RULE
purpose: Tỷ lệ sở hữu cổ phần
applies_to:
- shareholder_ownership_percentage
trigger: Khi cần điền field shareholder_ownership_percentage.
input_fields:
- shareholder_share_count
- total_share_count
- danh sách cổ đông
output_field: shareholder_ownership_percentage
processing_logic:
- Ưu tiên tỷ lệ trên danh sách cổ đông. Nếu thiếu, tính số cổ phần/tổng số cổ phần × 100. Tổng phải bằng 100%.
validation:
- 0--100%; tổng = 100%
- Tổng tỷ lệ sở hữu của cổ đông = 100%.
exceptions:
- Master đã có ký hiệu % ngay sau placeholder
```

---

## RULE_RULE_016 — member_capital_amount_words

```yaml
rule_id: RULE_RULE_016
rule_name: member_capital_amount_words
rule_type: RULE
purpose: Đổi vốn góp sang chữ
applies_to:
- member_capital_amount_words
trigger: Khi cần điền field member_capital_amount_words.
input_fields:
- member_capital_amount
output_field: member_capital_amount_words
processing_logic:
- Chuyển số tiền sang chữ tiếng Việt, viết hoa chữ cái đầu, kết thúc bằng 'đồng'; không thêm 'chẵn' trừ khi quy ước riêng.
validation:
- Khớp vốn góp bằng số
exceptions: []
```

---

## RULE_RULE_017 — shareholder_share_value_words

```yaml
rule_id: RULE_RULE_017
rule_name: shareholder_share_value_words
rule_type: RULE
purpose: Đổi giá trị cổ phần sang chữ
applies_to:
- shareholder_share_value_words
trigger: Khi cần điền field shareholder_share_value_words.
input_fields:
- shareholder_share_value
output_field: shareholder_share_value_words
processing_logic:
- Chuyển số tiền sang chữ tiếng Việt, chữ đầu viết hoa, đơn vị đồng.
validation:
- Khớp giá trị bằng số
exceptions: []
```

---

## RULE_RULE_018 — charter_capital_amount_words

```yaml
rule_id: RULE_RULE_018
rule_name: charter_capital_amount_words
rule_type: RULE
purpose: Đổi vốn điều lệ sang chữ
applies_to:
- charter_capital_amount_words
trigger: Khi cần điền field charter_capital_amount_words.
input_fields:
- charter_capital_amount
output_field: charter_capital_amount_words
processing_logic:
- Chuyển số tiền sang chữ tiếng Việt và đối chiếu với số.
validation:
- Khớp số tiền
exceptions: []
```

---

## RULE_RULE_019 — tax_code_digit_1

```yaml
rule_id: RULE_RULE_019
rule_name: tax_code_digit_1
rule_type: RULE
purpose: Tách MST từng ô
applies_to:
- tax_code_digit_1
trigger: Khi cần điền field tax_code_digit_1.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_1
processing_logic:
- Lấy ký tự thứ 1 của MST; mỗi placeholder chỉ nhận một ký tự; field vượt độ dài để trống.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_020 — tax_code_digit_2

```yaml
rule_id: RULE_RULE_020
rule_name: tax_code_digit_2
rule_type: RULE
purpose: Tách MST ký tự 2
applies_to:
- tax_code_digit_2
trigger: Khi cần điền field tax_code_digit_2.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_2
processing_logic:
- Lấy ký tự thứ 2 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_021 — tax_code_digit_3

```yaml
rule_id: RULE_RULE_021
rule_name: tax_code_digit_3
rule_type: RULE
purpose: Tách MST ký tự 3
applies_to:
- tax_code_digit_3
trigger: Khi cần điền field tax_code_digit_3.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_3
processing_logic:
- Lấy ký tự thứ 3 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_022 — tax_code_digit_4

```yaml
rule_id: RULE_RULE_022
rule_name: tax_code_digit_4
rule_type: RULE
purpose: Tách MST ký tự 4
applies_to:
- tax_code_digit_4
trigger: Khi cần điền field tax_code_digit_4.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_4
processing_logic:
- Lấy ký tự thứ 4 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_023 — tax_code_digit_5

```yaml
rule_id: RULE_RULE_023
rule_name: tax_code_digit_5
rule_type: RULE
purpose: Tách MST ký tự 5
applies_to:
- tax_code_digit_5
trigger: Khi cần điền field tax_code_digit_5.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_5
processing_logic:
- Lấy ký tự thứ 5 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_024 — tax_code_digit_6

```yaml
rule_id: RULE_RULE_024
rule_name: tax_code_digit_6
rule_type: RULE
purpose: Tách MST ký tự 6
applies_to:
- tax_code_digit_6
trigger: Khi cần điền field tax_code_digit_6.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_6
processing_logic:
- Lấy ký tự thứ 6 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_025 — tax_code_digit_7

```yaml
rule_id: RULE_RULE_025
rule_name: tax_code_digit_7
rule_type: RULE
purpose: Tách MST ký tự 7
applies_to:
- tax_code_digit_7
trigger: Khi cần điền field tax_code_digit_7.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_7
processing_logic:
- Lấy ký tự thứ 7 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_026 — tax_code_digit_8

```yaml
rule_id: RULE_RULE_026
rule_name: tax_code_digit_8
rule_type: RULE
purpose: Tách MST ký tự 8
applies_to:
- tax_code_digit_8
trigger: Khi cần điền field tax_code_digit_8.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_8
processing_logic:
- Lấy ký tự thứ 8 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_027 — tax_code_digit_9

```yaml
rule_id: RULE_RULE_027
rule_name: tax_code_digit_9
rule_type: RULE
purpose: Tách MST ký tự 9
applies_to:
- tax_code_digit_9
trigger: Khi cần điền field tax_code_digit_9.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_9
processing_logic:
- Lấy ký tự thứ 9 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_028 — tax_code_digit_10

```yaml
rule_id: RULE_RULE_028
rule_name: tax_code_digit_10
rule_type: RULE
purpose: Tách MST ký tự 10
applies_to:
- tax_code_digit_10
trigger: Khi cần điền field tax_code_digit_10.
input_fields:
- enterprise_tax_code
output_field: tax_code_digit_10
processing_logic:
- Lấy ký tự thứ 10 của MST; không điền toàn chuỗi vào một ô.
validation:
- Một chữ số
exceptions: []
```

---

## RULE_RULE_029 — member_block_begin_marker

```yaml
rule_id: RULE_RULE_029
rule_name: member_block_begin_marker
rule_type: RULE
purpose: Expand block thành viên
applies_to:
- member_block_begin_marker
trigger: Khi cần điền field member_block_begin_marker.
input_fields:
- member_list
output_field: member_block_begin_marker
processing_logic:
- Tìm cặp BEGIN/END trên toàn document tree.
- Nhân bản toàn block cho từng thành viên.
- Expand mọi occurrence.
- Xóa marker sau render.
- Giữ nguyên run/style.
validation:
- Không được chứa placeholder hoặc dữ liệu mẫu sau render.
exceptions:
- Placeholder bị split runs hoặc nằm trong table/header/footer/textbox
```

---

## RULE_RULE_030 — present_member_block_begin_marker

```yaml
rule_id: RULE_RULE_030
rule_name: present_member_block_begin_marker
rule_type: RULE
purpose: Expand block thành viên có mặt
applies_to:
- present_member_block_begin_marker
trigger: Khi cần điền field present_member_block_begin_marker.
input_fields:
- present_member_list
output_field: present_member_block_begin_marker
processing_logic:
- Thực hiện như block thành viên; mặc định present_member_list = member_list nếu không có dữ liệu vắng mặt.
validation:
- Không được chứa placeholder hoặc dữ liệu mẫu sau render.
exceptions:
- Có thành viên vắng mặt hoặc ủy quyền
```

---

## RULE_RULE_031 — shareholder_block_begin_marker

```yaml
rule_id: RULE_RULE_031
rule_name: shareholder_block_begin_marker
rule_type: RULE
purpose: Expand block cổ đông
applies_to:
- shareholder_block_begin_marker
trigger: Khi cần điền field shareholder_block_begin_marker.
input_fields:
- shareholder_list
output_field: shareholder_block_begin_marker
processing_logic:
- Tìm cặp BEGIN/END trên toàn tree.
- Với block trong bảng, nhân bản toàn hàng dữ liệu.
- Expand mọi occurrence bằng cùng nguồn danh sách.
- Xóa marker.
validation:
- Không được chứa placeholder hoặc dữ liệu mẫu sau render.
exceptions:
- Block cùng tên xuất hiện nhiều vị trí
```

---

## RULE_RULE_032 — director_name

```yaml
rule_id: RULE_RULE_032
rule_name: director_name
rule_type: RULE
purpose: Xác định người ký dưới nhãn Giám đốc
applies_to:
- director_name
trigger: Khi cần điền field director_name.
input_fields:
- legal_representative_name
- legal_representative_title
- USER_INPUT
output_field: director_name
processing_logic:
- Nếu NĐDPL có chức danh Giám đốc/Tổng giám đốc thì dùng NĐDPL. Nếu không, yêu cầu xác nhận người ký; không tự map.
validation:
- Khớp người ký thực tế
exceptions:
- NĐDPL không giữ chức Giám đốc
```

---

## RULE_RULE_033 — total_refund_value

```yaml
rule_id: RULE_RULE_033
rule_name: total_refund_value
rule_type: RULE
purpose: Tổng hoàn trả cổ đông
applies_to:
- total_refund_value
trigger: Khi cần điền field total_refund_value.
input_fields:
- total_remaining_asset_value
- chi tiết hoàn trả
output_field: total_refund_value
processing_logic:
- Trong workflow hiện tại, mặc định tổng hoàn trả bằng tổng tài sản còn lại; tổng chi tiết từng cổ đông phải bằng tổng hoàn trả.
validation:
- Tổng chi tiết hoàn trả = tổng hoàn trả
- Tổng hoàn trả phải bằng tổng chi tiết hoàn trả.
exceptions:
- Tài sản còn lại khác tổng vốn đã góp
```

---

## RULE_RULE_034 — shareholder_share_value

```yaml
rule_id: RULE_RULE_034
rule_name: shareholder_share_value
rule_type: RULE
purpose: Giá trị hoàn trả từng cổ đông
applies_to:
- shareholder_share_value
trigger: Khi cần điền field shareholder_share_value.
input_fields:
- shareholder_share_count
- share_par_value
output_field: shareholder_share_value
processing_logic:
- Trong bộ hồ sơ mặc định giá trị hoàn trả bằng giá trị cổ phần đã góp. Nếu có chi phí/lỗ/lãi làm thay đổi tài sản còn lại thì không áp dụng rule này.
validation:
- Khớp tỷ lệ và tổng giá trị
exceptions:
- Giá trị hoàn trả từng cổ đông khác giá trị cổ phần
```

---

## RULE_RULE_035 — first_member_name

```yaml
rule_id: RULE_RULE_035
rule_name: first_member_name
rule_type: RULE
purpose: Thành viên thứ nhất/chủ tọa
applies_to:
- first_member_name
trigger: Khi cần điền field first_member_name.
input_fields:
- member_list
- member_council_chairperson_name
output_field: first_member_name
processing_logic:
- Ưu tiên người được xác định là Chủ tịch HĐTV. Chỉ dùng phần tử thứ nhất nếu danh sách đã được sắp sao cho Chủ tịch ở vị trí đầu.
validation:
- Có trong danh sách thành viên
exceptions:
- Thành viên đầu danh sách không phải Chủ tịch HĐTV
```

---

## RULE_RULE_036 — generic_phone_number

```yaml
rule_id: RULE_RULE_036
rule_name: generic_phone_number
rule_type: RULE
purpose: Chọn số điện thoại theo ngữ cảnh
applies_to:
- generic_phone_number
trigger: Khi cần điền field generic_phone_number.
input_fields:
- master_id
- authorized_person_phone
- company_contact_phone
output_field: generic_phone_number
processing_logic:
- Giấy giới thiệu/ủy quyền → số của người được giới thiệu/ủy quyền. Công văn doanh nghiệp → số liên hệ doanh nghiệp. Nếu không xác định được vai trò, chặn render.
validation:
- Số điện thoại hợp lệ
exceptions:
- Không xác định placeholder thuộc cá nhân hay doanh nghiệp
```

---

## RULE_RULE_037 — generic_email

```yaml
rule_id: RULE_RULE_037
rule_name: generic_email
rule_type: RULE
purpose: Chọn email theo ngữ cảnh
applies_to:
- generic_email
trigger: Khi cần điền field generic_email.
input_fields:
- master_id
- authorized_person_email
- company_contact_email
output_field: generic_email
processing_logic:
- Giấy giới thiệu/ủy quyền → email người được giới thiệu/ủy quyền. Nếu master khác, xác nhận nguồn trước khi fill.
validation:
- Định dạng email
exceptions: []
```

---

## RULE_RULE_038 — total_remaining_asset_value

```yaml
rule_id: RULE_RULE_038
rule_name: total_remaining_asset_value
rule_type: RULE
purpose: Nguồn tài sản còn lại
applies_to:
- total_remaining_asset_value
trigger: Khi cần điền field total_remaining_asset_value.
input_fields:
- sổ sách
- biên bản thanh lý
- USER_INPUT
output_field: total_remaining_asset_value
processing_logic:
- Không suy từ vốn điều lệ nếu chưa có xác nhận. Dùng số liệu kế toán/biên bản hoặc người dùng xác nhận.
validation:
- Số \>= 0; định dạng nghìn
exceptions: []
```

---

## RULE_RULE_039 — authorized_person_id_issue_date

```yaml
rule_id: RULE_RULE_039
rule_name: authorized_person_id_issue_date
rule_type: RULE
purpose: Chọn chủ thể của CCCD
applies_to:
- authorized_person_id_issue_date
trigger: Khi cần điền field authorized_person_id_issue_date.
input_fields:
- master_id
- authorized_person profile
output_field: authorized_person_id_issue_date
processing_logic:
- Trong các master CTCP ủy quyền hiện tại, placeholder ngày cấp CCCD thuộc người được ủy quyền. Không dùng ngày cấp CCCD của Giám đốc.
validation:
- Ngày hợp lệ
exceptions:
- Master tái sử dụng cho CCCD Giám đốc
```

---

## RULE_RULE_040 — shareholder_share_type

```yaml
rule_id: RULE_RULE_040
rule_name: shareholder_share_type
rule_type: RULE
purpose: Loại cổ phần mặc định
applies_to:
- shareholder_share_type
trigger: Khi cần điền field shareholder_share_type.
input_fields:
- danh sách cổ đông
output_field: shareholder_share_type
processing_logic:
- Nếu tài liệu không nêu loại khác thì điền 'Phổ thông'. Nếu có cổ phần ưu đãi, dùng đúng loại trên tài liệu và chuyển kiểm tra quyền biểu quyết.
validation:
- Giá trị hợp lệ theo hồ sơ
exceptions:
- Có cổ phần ưu đãi hoặc quyền biểu quyết khác 1:1
```

---

## RULE_SEARCH_001 — business_registration_authority

```yaml
rule_id: RULE_SEARCH_001
rule_name: business_registration_authority
rule_type: SEARCH
purpose: Xác định tên cơ quan ĐKKD hiện hành
applies_to:
- business_registration_authority
trigger: Khi cần điền field business_registration_authority.
input_fields:
- registered_office_address
output_field: business_registration_authority
processing_logic:
- Chuẩn hóa tỉnh/thành từ địa chỉ.
- Tra tên phòng/cơ quan hiện hành.
- Đối chiếu ít nhất 2 nguồn nếu tên khác nhau.
- Lưu ngày tra cứu.
validation:
- Đúng tỉnh/thành và đúng tên cơ quan hiện hành
- Tên cơ quan phải là tên hiện hành tại thời điểm xuất hồ sơ.
exceptions:
- Địa chỉ GPKD dùng địa giới cũ
search_strategy:
- Cổng thông tin quốc gia về đăng ký doanh nghiệp; website chính thức UBND/Sở Tài chính tỉnh; văn bản tổ chức bộ máy hiện hành
```

---

## RULE_SEARCH_002 — tax_authority

```yaml
rule_id: RULE_SEARCH_002
rule_name: tax_authority
rule_type: SEARCH
purpose: Xác định cơ quan thuế quản lý trực tiếp
applies_to:
- tax_authority
trigger: Khi cần điền field tax_authority.
input_fields:
- enterprise_tax_code
- registered_office_address
output_field: tax_authority
processing_logic:
- Tra theo MST.
- Đối chiếu địa chỉ trụ sở.
- Xác định cơ quan quản lý trực tiếp sau sắp xếp tổ chức.
- Lưu nguồn và ngày tra cứu.
validation:
- Khớp địa bàn, MST và cơ quan quản lý hiện hành
- Cơ quan thuế phải khớp MST và địa bàn hiện hành.
exceptions:
- Cơ quan thuế trên hồ sơ cũ khác kết quả tra hiện hành
search_strategy:
- Cổng thông tin/website chính thức cơ quan thuế; thông tin tra cứu MST; thông báo của cơ quan thuế do doanh nghiệp cung cấp
```

---

## RULE_SEARCH_003 — customs_authority

```yaml
rule_id: RULE_SEARCH_003
rule_name: customs_authority
rule_type: SEARCH
purpose: Xác định cơ quan hải quan tiếp nhận
applies_to:
- customs_authority
trigger: Khi cần điền field customs_authority.
input_fields:
- registered_office_address
- enterprise_tax_code
- import_export_status
output_field: customs_authority
processing_logic:
- Xác định tỉnh/khu vực.
- Kiểm tra tình trạng phát sinh XNK nếu có dữ liệu.
- Nếu chưa phát sinh XNK, chọn chi cục/khu vực quản lý doanh nghiệp theo địa bàn và ghi note.
- Lưu nguồn.
validation:
- Tên cơ quan hiện hành; đúng khu vực
- Cơ quan hải quan phải đúng khu vực quản lý hiện hành.
exceptions:
- Doanh nghiệp từng phát sinh XNK
search_strategy:
- Website Tổng cục Hải quan/Cục Hải quan khu vực; hướng dẫn tiếp nhận chính thức
```

---

## RULE_COMPANY_INTERNAL_ABBREVIATION — company_internal_abbreviation

```yaml
rule_id: RULE_COMPANY_INTERNAL_ABBREVIATION
rule_name: company_internal_abbreviation
rule_type: RULE
purpose: Sinh giá trị cho placeholder [VIẾT TẮT CÔNG TY] theo quy ước nội bộ.
applies_to:
- company_internal_abbreviation
trigger: Khi cần điền placeholder [VIẾT TẮT CÔNG TY] hoặc field company_internal_abbreviation.
input_fields:
- company_name
output_field: company_internal_abbreviation
processing_logic:
- Dựa trên company_name.
- Xác định phần tên riêng chính của doanh nghiệp.
- Lấy chữ cái đầu của từng từ trong phần tên riêng.
- Viết hoa kết quả.
- Không dùng loại hình doanh nghiệp hoặc phần mô tả ngành nghề.
- Không lấy company_name_en hoặc tên viết tắt tiếng Anh trên GPKD.
- 'Ví dụ: HUY HOÀNG -> HH.'
- 'Ví dụ: NAM KHÁNH -> NK.'
- 'Ví dụ: CÔNG TY CỔ PHẦN XÂY DỰNG DV&TM MINH NGỌC -> tên riêng: MINH NGỌC -> company_internal_abbreviation: MN.'
validation:
- Kết quả viết hoa.
- Kết quả chỉ được suy ra từ phần tên riêng chính của company_name.
- Không sử dụng loại hình doanh nghiệp, phần mô tả ngành nghề, company_name_en hoặc tên viết tắt tiếng Anh trên GPKD.
exceptions:
- 'Nếu không xác định chắc chắn phần tên riêng: không tự đoán; đưa vào needs_confirmation.'
```

---

# NEEDS_CONFIRMATION

## director_name

-   **item_id**: NC-001
-   **related_field**: director_name
-   **issue**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều có
    NĐDPL giữ chức Giám đốc.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## generic_person_name
-   **item_id**: NC-002
-   **related_field**: generic_person_name
-   **issue**: Xuất hiện trong câu hướng dẫn thêm block profile, chưa
    xác định có được render hay chỉ là ví dụ.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: generic_person_name; không phải field runtime
-   **recommendation**: Không tự fill cho đến khi xác nhận. \##
    person_honorific
-   **item_id**: NC-003
-   **related_field**: person_honorific
-   **issue**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## present_shareholder_block_begin_marker
-   **item_id**: NC-004
-   **related_field**: present_shareholder_block_begin_marker
-   **issue**: Marker cũ đã được đổi thành BEGIN_CO_DONG ở master chốt
    sau.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: Giữ marker riêng; alias với shareholder block
-   **recommendation**: Không tự thay master; mapping riêng và ghi phiên
    bản cũ.

## present_shareholder_block_end_marker
-   **item_id**: NC-005
-   **related_field**: present_shareholder_block_end_marker
-   **issue**: Marker cũ đã được đổi thành END_CO_DONG ở master chốt
    sau.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: Giữ marker riêng; alias với shareholder block
-   **recommendation**: Không tự thay master; mapping riêng và ghi phiên
    bản cũ.

## shareholder_sequence_number
-   **item_id**: NC-006
-   **related_field**: shareholder_sequence_number
-   **issue**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## total_voting_rights_count
-   **item_id**: NC-007
-   **related_field**: total_voting_rights_count
-   **issue**: TNHH dùng vốn điều lệ/10.000; CTCP dùng tổng cổ phần có
    quyền biểu quyết.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: Tách canonical theo loại hình; giữ canonical dùng chung
    có company_type
-   **recommendation**: v0.1 giữ total_voting_rights_count và áp rule
    theo company_type.

## total_voting_rights_count
-   **item_id**: NC-008
-   **related_field**: total_voting_rights_count
-   **issue**: Một canonical đang bao phủ hai công thức theo loại hình.
-   **current_understanding**: Rulebook áp company_type để chọn công
    thức.
-   **options**: Tách thành total_voting_ballots_tnhh và
    total_votes_present; giữ field chung.
-   **recommendation**: Khi xây Rulebook v1.0 nên tách canonical hoặc
    thêm discriminator company_type.

## director_name
-   **item_id**: NC-009
-   **related_field**: director_name
-   **issue**: Tên field lịch sử 'Giám đốc' có thể không đúng chức danh
    NĐDPL.
-   **current_understanding**: Hiện dùng COMPOSITE và manual review khi
    chức danh khác.
-   **options**: Đổi master; giữ alias; tạo signing_person_name.
-   **recommendation**: v0.1 giữ alias, không sửa master. \##
    shareholder_share_value
-   **item_id**: NC-010
-   **related_field**: shareholder_share_value
-   **issue**: Rule giá trị hoàn trả = giá trị vốn góp chỉ đúng với bộ
    hồ sơ mặc định.
-   **current_understanding**: Đã ghi exception khi tài sản còn lại khác
    vốn góp.
-   **options**: Giữ một field; tách refund field.
-   **recommendation**: Theo dõi khi vận hành; tách ở v0.2 nếu có hồ sơ
    ngoại lệ.

---

## MIGRATION_CHECK

- total_rules_old: 43
- total_rules_new: 44
- rules_added: [RULE_COMPANY_INTERNAL_ABBREVIATION]
- rules_removed: []
- business_logic_changed: false
