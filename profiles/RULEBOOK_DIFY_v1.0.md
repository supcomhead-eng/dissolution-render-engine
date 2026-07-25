# RULEBOOK_DIFY_v1.0

------------------------------------------------------------------------

# Rule: company_name

**Rule ID:** RULE_RULE_001

## Rule Type

RULE

## Purpose

Ưu tiên nguồn dữ liệu doanh nghiệp

## Applies To

company_name

## Trigger

Khi cần điền field company_name.

## Input Fields

GPKD, CCCD/VNeID, USER_INPUT

## Output Field

company_name

## Processing Logic

1)  Đọc tên doanh nghiệp từ GPKD. 2) Không lấy tên doanh nghiệp từ
    CCCD. 3) Nếu GPKD mờ/thiếu, yêu cầu người dùng cung cấp lại; không
    tự đoán.

## Validation

-   Không rỗng; đối chiếu cùng MST

------------------------------------------------------------------------

# Rule: legal_representative_name

**Rule ID:** RULE_RULE_002

## Rule Type

RULE

## Purpose

Ưu tiên dữ liệu nhân thân

## Applies To

legal_representative_name

## Trigger

Khi cần điền field legal_representative_name.

## Input Fields

GPKD, CCCD/VNeID

## Output Field

legal_representative_name

## Processing Logic

1)  Xác định NĐDPL trên GPKD. 2) Đối chiếu họ tên với CCCD/VNeID. 3) Nếu
    khác về dữ liệu nhân thân, ưu tiên CCCD/VNeID và ghi log sai
    khác. 4) Không đổi vai trò NĐDPL nếu GPKD không xác nhận.

## Validation

-   Không rỗng; viết hoa theo master khi cần

## Exception

-   CCCD/VNeID khác GPKD về họ tên/ngày sinh/CCCD

------------------------------------------------------------------------

# Rule: authorized_person_name

**Rule ID:** RULE_RULE_003

## Rule Type

RULE

## Purpose

Lấy hồ sơ người được ủy quyền

## Applies To

authorized_person_name

## Trigger

Khi cần điền field authorized_person_name.

## Input Fields

CCCD/VNeID, profile ủy quyền, USER_INPUT

## Output Field

authorized_person_name

## Processing Logic

1)  Ưu tiên profile đã chốt. 2) Đối chiếu CCCD/VNeID nếu có. 3) Nếu
    người dùng chọn profile khác, dùng đúng profile được chỉ định. 4)
    Không thay người được ủy quyền bằng người khác.

## Validation

-   Khớp CCCD

------------------------------------------------------------------------

# Rule: document_year

**Rule ID:** RULE_RULE_004

## Rule Type

RULE

## Purpose

Xác định năm văn bản

## Applies To

document_year

## Trigger

Khi cần điền field document_year.

## Input Fields

Ngày hệ thống, USER_INPUT

## Output Field

document_year

## Processing Logic

1)  Nếu người dùng chỉ định năm hồ sơ thì dùng năm đó. 2) Nếu không,
    dùng năm hiện hành của hệ thống. 3) Không tự điền ngày/tháng nếu
    master chủ ý để trống.

## Validation

-   4 chữ số
-   Năm phải là 4 chữ số và nhất quán trong cùng bộ hồ sơ.

## Exception

-   Người dùng yêu cầu ngày ký để trống

------------------------------------------------------------------------

# Rule: signing_place

**Rule ID:** RULE_RULE_005

## Rule Type

RULE

## Purpose

Suy luận nơi ký

## Applies To

signing_place

## Trigger

Khi cần điền field signing_place.

## Input Fields

registered_office_address

## Output Field

signing_place

## Processing Logic

1)  Chuẩn hóa địa giới hiện hành của trụ sở. 2) Lấy tỉnh/thành phố trực
    thuộc trung ương. 3) Ghi theo cách dùng trong master, không tự thêm
    cấp quận/huyện.

## Validation

-   Phù hợp địa giới hành chính hiện hành

------------------------------------------------------------------------

# Rule: person_honorific

**Rule ID:** RULE_RULE_006

## Rule Type

RULE

## Purpose

Suy luận Ông/Bà

## Applies To

person_honorific

## Trigger

Khi cần điền field person_honorific.

## Input Fields

person_gender

## Output Field

person_honorific

## Processing Logic

1)  Xác định đúng chủ thể ngay sau placeholder. 2) Nam → Ông. 3) Nữ →
    Bà. 4) Không suy từ tên khi thiếu giới tính.

## Validation

-   Chỉ Ông hoặc Bà
-   Không được điền Ông/Bà khi chưa xác định giới tính của đúng chủ thể.

## Exception

-   Thiếu giới tính

------------------------------------------------------------------------

# Rule: company_abbreviation

**Rule ID:** RULE_RULE_007

## Rule Type

RULE

## Purpose

Lấy tên viết tắt

## Applies To

company_abbreviation

## Trigger

Khi cần điền field company_abbreviation.

## Input Fields

GPKD, USER_INPUT

## Output Field

company_abbreviation

## Processing Logic

1)  Dùng tên viết tắt ghi trên GPKD. 2) Nếu không có, yêu cầu người dùng
    nhập. 3) Không tự ghép chữ cái đầu.

## Validation

-   Không chứa ký tự đường dẫn

## Exception

-   GPKD không có tên viết tắt

------------------------------------------------------------------------

# Rule: employee_count

**Rule ID:** RULE_RULE_008

## Rule Type

RULE

## Purpose

Mặc định số lao động

## Applies To

employee_count

## Trigger

Khi cần điền field employee_count.

## Input Fields

Dữ liệu thực tế, CONSTANT

## Output Field

employee_count

## Processing Logic

1)  Nếu hồ sơ thực tế có số lao động thì dùng số thực tế. 2) Nếu không
    có dữ liệu và workflow hồ sơ chuẩn áp dụng, dùng 0. 3) Không dùng
    placeholder để trống.

## Validation

-   Số nguyên \>= 0

## Exception

-   Doanh nghiệp còn lao động hoặc có nghĩa vụ lao động

------------------------------------------------------------------------

# Rule: share_par_value

**Rule ID:** RULE_RULE_009

## Rule Type

RULE

## Purpose

Mệnh giá cổ phần mặc định

## Applies To

share_par_value

## Trigger

Khi cần điền field share_par_value.

## Input Fields

GPKD/danh sách cổ đông, CONSTANT

## Output Field

share_par_value

## Processing Logic

1)  Nếu hồ sơ ghi mệnh giá thì dùng giá trị hồ sơ. 2) Nếu không ghi, mặc
    định 10.000 đồng/cổ phần.

## Validation

-   10.000, trừ khi giấy tờ thể hiện khác

------------------------------------------------------------------------

# Rule: shareholder_share_value

**Rule ID:** RULE_RULE_010

## Rule Type

RULE

## Purpose

Tính giá trị cổ phần

## Applies To

shareholder_share_value

## Trigger

Khi cần điền field shareholder_share_value.

## Input Fields

shareholder_share_count, share_par_value

## Output Field

shareholder_share_value

## Processing Logic

Nhân số cổ phần với mệnh giá; làm tròn về số nguyên đồng; định dạng dấu
chấm phân tách nghìn.

## Validation

-   Khớp tỷ lệ và tổng giá trị

## Exception

-   Giá trị hoàn trả từng cổ đông khác giá trị cổ phần

------------------------------------------------------------------------

# Rule: shareholder_vote_count

**Rule ID:** RULE_RULE_011

## Rule Type

RULE

## Purpose

Tính phiếu biểu quyết cổ đông

## Applies To

shareholder_vote_count

## Trigger

Khi cần điền field shareholder_vote_count.

## Input Fields

shareholder_share_count, shareholder_share_type

## Output Field

shareholder_vote_count

## Processing Logic

Nếu loại cổ phần là Phổ thông thì số phiếu bằng số cổ phần. Nếu loại
khác, không tự tính và chuyển NEEDS_CONFIRMATION.

## Validation

-   Số nguyên \>= 0

------------------------------------------------------------------------

# Rule: total_votes_present

**Rule ID:** RULE_RULE_012

## Rule Type

RULE

## Purpose

Tổng phiếu dự họp CTCP

## Applies To

total_votes_present

## Trigger

Khi cần điền field total_votes_present.

## Input Fields

shareholder_vote_count của cổ đông dự họp

## Output Field

total_votes_present

## Processing Logic

Cộng số phiếu của tất cả cổ đông được đánh dấu có mặt/được tính quyền
biểu quyết. Workflow hiện tại mặc định toàn bộ cổ đông có mặt và đạt
100%.

## Validation

-   Số nguyên; khớp tổng cổ phần dự họp
-   Tổng phiếu phải bằng tổng phiếu của cổ đông dự họp.

------------------------------------------------------------------------

# Rule: total_voting_ballots_tnhh

**Rule ID:** RULE_RULE_013

## Rule Type

RULE

## Purpose

Tổng phiếu biểu quyết TNHH

## Applies To

total_voting_ballots_tnhh

## Trigger

Khi cần điền field total_voting_ballots_tnhh.

## Input Fields

charter_capital_amount

## Output Field

total_voting_ballots_tnhh

## Processing Logic

Chia tổng vốn điều lệ cho 10.000; kết quả phải là số nguyên; định dạng
phân tách nghìn.

------------------------------------------------------------------------

# Rule: member_capital_ratio

**Rule ID:** RULE_RULE_014

## Rule Type

RULE

## Purpose

Tỷ lệ góp vốn

## Applies To

member_capital_ratio

## Trigger

Khi cần điền field member_capital_ratio.

## Input Fields

member_capital_amount, charter_capital_amount, GPKD

## Output Field

member_capital_ratio

## Processing Logic

Ưu tiên tỷ lệ trên GPKD. Nếu thiếu, tính vốn góp/tổng vốn × 100. Tổng
các thành viên phải bằng 100%.

## Validation

-   0--100%; tổng danh sách = 100%
-   Tổng tỷ lệ góp vốn của toàn bộ thành viên = 100%.

## Exception

-   Master không có ký hiệu % ngoài placeholder

------------------------------------------------------------------------

# Rule: shareholder_ownership_percentage

**Rule ID:** RULE_RULE_015

## Rule Type

RULE

## Purpose

Tỷ lệ sở hữu cổ phần

## Applies To

shareholder_ownership_percentage

## Trigger

Khi cần điền field shareholder_ownership_percentage.

## Input Fields

shareholder_share_count, total_share_count, danh sách cổ đông

## Output Field

shareholder_ownership_percentage

## Processing Logic

Ưu tiên tỷ lệ trên danh sách cổ đông. Nếu thiếu, tính số cổ phần/tổng số
cổ phần × 100. Tổng phải bằng 100%.

## Validation

-   0--100%; tổng = 100%
-   Tổng tỷ lệ sở hữu của cổ đông = 100%.

## Exception

-   Master đã có ký hiệu % ngay sau placeholder

------------------------------------------------------------------------

# Rule: member_capital_amount_words

**Rule ID:** RULE_RULE_016

## Rule Type

RULE

## Purpose

Đổi vốn góp sang chữ

## Applies To

member_capital_amount_words

## Trigger

Khi cần điền field member_capital_amount_words.

## Input Fields

member_capital_amount

## Output Field

member_capital_amount_words

## Processing Logic

Chuyển số tiền sang chữ tiếng Việt, viết hoa chữ cái đầu, kết thúc bằng
'đồng'; không thêm 'chẵn' trừ khi quy ước riêng.

## Validation

-   Khớp vốn góp bằng số

------------------------------------------------------------------------

# Rule: shareholder_share_value_words

**Rule ID:** RULE_RULE_017

## Rule Type

RULE

## Purpose

Đổi giá trị cổ phần sang chữ

## Applies To

shareholder_share_value_words

## Trigger

Khi cần điền field shareholder_share_value_words.

## Input Fields

shareholder_share_value

## Output Field

shareholder_share_value_words

## Processing Logic

Chuyển số tiền sang chữ tiếng Việt, chữ đầu viết hoa, đơn vị đồng.

## Validation

-   Khớp giá trị bằng số

------------------------------------------------------------------------

# Rule: charter_capital_amount_words

**Rule ID:** RULE_RULE_018

## Rule Type

RULE

## Purpose

Đổi vốn điều lệ sang chữ

## Applies To

charter_capital_amount_words

## Trigger

Khi cần điền field charter_capital_amount_words.

## Input Fields

charter_capital_amount

## Output Field

charter_capital_amount_words

## Processing Logic

Chuyển số tiền sang chữ tiếng Việt và đối chiếu với số.

## Validation

-   Khớp số tiền

------------------------------------------------------------------------

# Rule: tax_code_digit_1

**Rule ID:** RULE_RULE_019

## Rule Type

RULE

## Purpose

Tách MST từng ô

## Applies To

tax_code_digit_1

## Trigger

Khi cần điền field tax_code_digit_1.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_1

## Processing Logic

Lấy ký tự thứ 1 của MST; mỗi placeholder chỉ nhận một ký tự; field vượt
độ dài để trống.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_2

**Rule ID:** RULE_RULE_020

## Rule Type

RULE

## Purpose

Tách MST ký tự 2

## Applies To

tax_code_digit_2

## Trigger

Khi cần điền field tax_code_digit_2.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_2

## Processing Logic

Lấy ký tự thứ 2 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_3

**Rule ID:** RULE_RULE_021

## Rule Type

RULE

## Purpose

Tách MST ký tự 3

## Applies To

tax_code_digit_3

## Trigger

Khi cần điền field tax_code_digit_3.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_3

## Processing Logic

Lấy ký tự thứ 3 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_4

**Rule ID:** RULE_RULE_022

## Rule Type

RULE

## Purpose

Tách MST ký tự 4

## Applies To

tax_code_digit_4

## Trigger

Khi cần điền field tax_code_digit_4.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_4

## Processing Logic

Lấy ký tự thứ 4 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_5

**Rule ID:** RULE_RULE_023

## Rule Type

RULE

## Purpose

Tách MST ký tự 5

## Applies To

tax_code_digit_5

## Trigger

Khi cần điền field tax_code_digit_5.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_5

## Processing Logic

Lấy ký tự thứ 5 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_6

**Rule ID:** RULE_RULE_024

## Rule Type

RULE

## Purpose

Tách MST ký tự 6

## Applies To

tax_code_digit_6

## Trigger

Khi cần điền field tax_code_digit_6.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_6

## Processing Logic

Lấy ký tự thứ 6 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_7

**Rule ID:** RULE_RULE_025

## Rule Type

RULE

## Purpose

Tách MST ký tự 7

## Applies To

tax_code_digit_7

## Trigger

Khi cần điền field tax_code_digit_7.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_7

## Processing Logic

Lấy ký tự thứ 7 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_8

**Rule ID:** RULE_RULE_026

## Rule Type

RULE

## Purpose

Tách MST ký tự 8

## Applies To

tax_code_digit_8

## Trigger

Khi cần điền field tax_code_digit_8.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_8

## Processing Logic

Lấy ký tự thứ 8 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_9

**Rule ID:** RULE_RULE_027

## Rule Type

RULE

## Purpose

Tách MST ký tự 9

## Applies To

tax_code_digit_9

## Trigger

Khi cần điền field tax_code_digit_9.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_9

## Processing Logic

Lấy ký tự thứ 9 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: tax_code_digit_10

**Rule ID:** RULE_RULE_028

## Rule Type

RULE

## Purpose

Tách MST ký tự 10

## Applies To

tax_code_digit_10

## Trigger

Khi cần điền field tax_code_digit_10.

## Input Fields

enterprise_tax_code

## Output Field

tax_code_digit_10

## Processing Logic

Lấy ký tự thứ 10 của MST; không điền toàn chuỗi vào một ô.

## Validation

-   Một chữ số

------------------------------------------------------------------------

# Rule: member_block_begin_marker

**Rule ID:** RULE_RULE_029

## Rule Type

RULE

## Purpose

Expand block thành viên

## Applies To

member_block_begin_marker

## Trigger

Khi cần điền field member_block_begin_marker.

## Input Fields

member_list

## Output Field

member_block_begin_marker

## Processing Logic

1)  Tìm cặp BEGIN/END trên toàn document tree. 2) Nhân bản toàn block
    cho từng thành viên. 3) Expand mọi occurrence. 4) Xóa marker sau
    render. 5) Giữ nguyên run/style.

## Validation

-   Không được chứa placeholder hoặc dữ liệu mẫu sau render.

## Exception

-   Placeholder bị split runs hoặc nằm trong table/header/footer/textbox

------------------------------------------------------------------------

# Rule: present_member_block_begin_marker

**Rule ID:** RULE_RULE_030

## Rule Type

RULE

## Purpose

Expand block thành viên có mặt

## Applies To

present_member_block_begin_marker

## Trigger

Khi cần điền field present_member_block_begin_marker.

## Input Fields

present_member_list

## Output Field

present_member_block_begin_marker

## Processing Logic

Thực hiện như block thành viên; mặc định present_member_list =
member_list nếu không có dữ liệu vắng mặt.

## Validation

-   Không được chứa placeholder hoặc dữ liệu mẫu sau render.

## Exception

-   Có thành viên vắng mặt hoặc ủy quyền

------------------------------------------------------------------------

# Rule: shareholder_block_begin_marker

**Rule ID:** RULE_RULE_031

## Rule Type

RULE

## Purpose

Expand block cổ đông

## Applies To

shareholder_block_begin_marker

## Trigger

Khi cần điền field shareholder_block_begin_marker.

## Input Fields

shareholder_list

## Output Field

shareholder_block_begin_marker

## Processing Logic

1)  Tìm cặp BEGIN/END trên toàn tree. 2) Với block trong bảng, nhân bản
    toàn hàng dữ liệu. 3) Expand mọi occurrence bằng cùng nguồn danh
    sách. 4) Xóa marker.

## Validation

-   Không được chứa placeholder hoặc dữ liệu mẫu sau render.

## Exception

-   Block cùng tên xuất hiện nhiều vị trí

------------------------------------------------------------------------

# Rule: director_name

**Rule ID:** RULE_RULE_032

## Rule Type

RULE

## Purpose

Xác định người ký dưới nhãn Giám đốc

## Applies To

director_name

## Trigger

Khi cần điền field director_name.

## Input Fields

legal_representative_name, legal_representative_title, USER_INPUT

## Output Field

director_name

## Processing Logic

Nếu NĐDPL có chức danh Giám đốc/Tổng giám đốc thì dùng NĐDPL. Nếu không,
yêu cầu xác nhận người ký; không tự map.

## Validation

-   Khớp người ký thực tế

## Exception

-   NĐDPL không giữ chức Giám đốc

------------------------------------------------------------------------

# Rule: total_refund_value

**Rule ID:** RULE_RULE_033

## Rule Type

RULE

## Purpose

Tổng hoàn trả cổ đông

## Applies To

total_refund_value

## Trigger

Khi cần điền field total_refund_value.

## Input Fields

total_remaining_asset_value, chi tiết hoàn trả

## Output Field

total_refund_value

## Processing Logic

Trong workflow hiện tại, mặc định tổng hoàn trả bằng tổng tài sản còn
lại; tổng chi tiết từng cổ đông phải bằng tổng hoàn trả.

## Validation

-   Tổng chi tiết hoàn trả = tổng hoàn trả
-   Tổng hoàn trả phải bằng tổng chi tiết hoàn trả.

## Exception

-   Tài sản còn lại khác tổng vốn đã góp

------------------------------------------------------------------------

# Rule: shareholder_share_value

**Rule ID:** RULE_RULE_034

## Rule Type

RULE

## Purpose

Giá trị hoàn trả từng cổ đông

## Applies To

shareholder_share_value

## Trigger

Khi cần điền field shareholder_share_value.

## Input Fields

shareholder_share_count, share_par_value

## Output Field

shareholder_share_value

## Processing Logic

Trong bộ hồ sơ mặc định giá trị hoàn trả bằng giá trị cổ phần đã góp.
Nếu có chi phí/lỗ/lãi làm thay đổi tài sản còn lại thì không áp dụng
rule này.

## Validation

-   Khớp tỷ lệ và tổng giá trị

## Exception

-   Giá trị hoàn trả từng cổ đông khác giá trị cổ phần

------------------------------------------------------------------------

# Rule: first_member_name

**Rule ID:** RULE_RULE_035

## Rule Type

RULE

## Purpose

Thành viên thứ nhất/chủ tọa

## Applies To

first_member_name

## Trigger

Khi cần điền field first_member_name.

## Input Fields

member_list, member_council_chairperson_name

## Output Field

first_member_name

## Processing Logic

Ưu tiên người được xác định là Chủ tịch HĐTV. Chỉ dùng phần tử thứ nhất
nếu danh sách đã được sắp sao cho Chủ tịch ở vị trí đầu.

## Validation

-   Có trong danh sách thành viên

## Exception

-   Thành viên đầu danh sách không phải Chủ tịch HĐTV

------------------------------------------------------------------------

# Rule: generic_phone_number

**Rule ID:** RULE_RULE_036

## Rule Type

RULE

## Purpose

Chọn số điện thoại theo ngữ cảnh

## Applies To

generic_phone_number

## Trigger

Khi cần điền field generic_phone_number.

## Input Fields

master_id, authorized_person_phone, company_contact_phone

## Output Field

generic_phone_number

## Processing Logic

Giấy giới thiệu/ủy quyền → số của người được giới thiệu/ủy quyền. Công
văn doanh nghiệp → số liên hệ doanh nghiệp. Nếu không xác định được vai
trò, chặn render.

## Validation

-   Số điện thoại hợp lệ

## Exception

-   Không xác định placeholder thuộc cá nhân hay doanh nghiệp

------------------------------------------------------------------------

# Rule: generic_email

**Rule ID:** RULE_RULE_037

## Rule Type

RULE

## Purpose

Chọn email theo ngữ cảnh

## Applies To

generic_email

## Trigger

Khi cần điền field generic_email.

## Input Fields

master_id, authorized_person_email, company_contact_email

## Output Field

generic_email

## Processing Logic

Giấy giới thiệu/ủy quyền → email người được giới thiệu/ủy quyền. Nếu
master khác, xác nhận nguồn trước khi fill.

## Validation

-   Định dạng email

------------------------------------------------------------------------

# Rule: total_remaining_asset_value

**Rule ID:** RULE_RULE_038

## Rule Type

RULE

## Purpose

Nguồn tài sản còn lại

## Applies To

total_remaining_asset_value

## Trigger

Khi cần điền field total_remaining_asset_value.

## Input Fields

sổ sách, biên bản thanh lý, USER_INPUT

## Output Field

total_remaining_asset_value

## Processing Logic

Không suy từ vốn điều lệ nếu chưa có xác nhận. Dùng số liệu kế toán/biên
bản hoặc người dùng xác nhận.

## Validation

-   Số \>= 0; định dạng nghìn

------------------------------------------------------------------------

# Rule: authorized_person_id_issue_date

**Rule ID:** RULE_RULE_039

## Rule Type

RULE

## Purpose

Chọn chủ thể của CCCD

## Applies To

authorized_person_id_issue_date

## Trigger

Khi cần điền field authorized_person_id_issue_date.

## Input Fields

master_id, authorized_person profile

## Output Field

authorized_person_id_issue_date

## Processing Logic

Trong các master CTCP ủy quyền hiện tại, placeholder ngày cấp CCCD thuộc
người được ủy quyền. Không dùng ngày cấp CCCD của Giám đốc.

## Validation

-   Ngày hợp lệ

## Exception

-   Master tái sử dụng cho CCCD Giám đốc

------------------------------------------------------------------------

# Rule: shareholder_share_type

**Rule ID:** RULE_RULE_040

## Rule Type

RULE

## Purpose

Loại cổ phần mặc định

## Applies To

shareholder_share_type

## Trigger

Khi cần điền field shareholder_share_type.

## Input Fields

danh sách cổ đông

## Output Field

shareholder_share_type

## Processing Logic

Nếu tài liệu không nêu loại khác thì điền 'Phổ thông'. Nếu có cổ phần ưu
đãi, dùng đúng loại trên tài liệu và chuyển kiểm tra quyền biểu quyết.

## Validation

-   Giá trị hợp lệ theo hồ sơ

## Exception

-   Có cổ phần ưu đãi hoặc quyền biểu quyết khác 1:1

------------------------------------------------------------------------

# Rule: business_registration_authority

**Rule ID:** RULE_SEARCH_001

## Rule Type

SEARCH

## Purpose

Xác định tên cơ quan ĐKKD hiện hành

## Applies To

business_registration_authority

## Trigger

Khi cần điền field business_registration_authority.

## Input Fields

registered_office_address

## Output Field

business_registration_authority

## Processing Logic

1)  Chuẩn hóa tỉnh/thành từ địa chỉ. 2) Tra tên phòng/cơ quan hiện
    hành. 3) Đối chiếu ít nhất 2 nguồn nếu tên khác nhau. 4) Lưu ngày
    tra cứu.

## Search Strategy

Cổng thông tin quốc gia về đăng ký doanh nghiệp; website chính thức
UBND/Sở Tài chính tỉnh; văn bản tổ chức bộ máy hiện hành

## Validation

-   Đúng tỉnh/thành và đúng tên cơ quan hiện hành
-   Tên cơ quan phải là tên hiện hành tại thời điểm xuất hồ sơ.

## Exception

-   Địa chỉ GPKD dùng địa giới cũ

------------------------------------------------------------------------

# Rule: tax_authority

**Rule ID:** RULE_SEARCH_002

## Rule Type

SEARCH

## Purpose

Xác định cơ quan thuế quản lý trực tiếp

## Applies To

tax_authority

## Trigger

Khi cần điền field tax_authority.

## Input Fields

enterprise_tax_code, registered_office_address

## Output Field

tax_authority

## Processing Logic

1)  Tra theo MST. 2) Đối chiếu địa chỉ trụ sở. 3) Xác định cơ quan quản
    lý trực tiếp sau sắp xếp tổ chức. 4) Lưu nguồn và ngày tra cứu.

## Search Strategy

Cổng thông tin/website chính thức cơ quan thuế; thông tin tra cứu MST;
thông báo của cơ quan thuế do doanh nghiệp cung cấp

## Validation

-   Khớp địa bàn, MST và cơ quan quản lý hiện hành
-   Cơ quan thuế phải khớp MST và địa bàn hiện hành.

## Exception

-   Cơ quan thuế trên hồ sơ cũ khác kết quả tra hiện hành

------------------------------------------------------------------------

# Rule: customs_authority

**Rule ID:** RULE_SEARCH_003

## Rule Type

SEARCH

## Purpose

Xác định cơ quan hải quan tiếp nhận

## Applies To

customs_authority

## Trigger

Khi cần điền field customs_authority.

## Input Fields

registered_office_address, enterprise_tax_code, import_export_status

## Output Field

customs_authority

## Processing Logic

1)  Xác định tỉnh/khu vực. 2) Kiểm tra tình trạng phát sinh XNK nếu có
    dữ liệu. 3) Nếu chưa phát sinh XNK, chọn chi cục/khu vực quản lý
    doanh nghiệp theo địa bàn và ghi note. 4) Lưu nguồn.

## Search Strategy

Website Tổng cục Hải quan/Cục Hải quan khu vực; hướng dẫn tiếp nhận
chính thức

## Validation

-   Tên cơ quan hiện hành; đúng khu vực
-   Cơ quan hải quan phải đúng khu vực quản lý hiện hành.

## Exception

-   Doanh nghiệp từng phát sinh XNK

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
    khi chức danh không phải Giám đốc. \## generic_person_name
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
    định vai trò theo vị trí. \## present_shareholder_block_begin_marker
-   **item_id**: NC-004
-   **related_field**: present_shareholder_block_begin_marker
-   **issue**: Marker cũ đã được đổi thành BEGIN_CO_DONG ở master chốt
    sau.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: Giữ marker riêng; alias với shareholder block
-   **recommendation**: Không tự thay master; mapping riêng và ghi phiên
    bản cũ. \## present_shareholder_block_end_marker
-   **item_id**: NC-005
-   **related_field**: present_shareholder_block_end_marker
-   **issue**: Marker cũ đã được đổi thành END_CO_DONG ở master chốt
    sau.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: Giữ marker riêng; alias với shareholder block
-   **recommendation**: Không tự thay master; mapping riêng và ghi phiên
    bản cũ. \## shareholder_sequence_number
-   **item_id**: NC-006
-   **related_field**: shareholder_sequence_number
-   **issue**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh. \## total_voting_rights_count
-   **item_id**: NC-007
-   **related_field**: total_voting_rights_count
-   **issue**: TNHH dùng vốn điều lệ/10.000; CTCP dùng tổng cổ phần có
    quyền biểu quyết.
-   **current_understanding**: Đã có mapping v0.1 nhưng cần review theo
    ngữ cảnh master.
-   **options**: Tách canonical theo loại hình; giữ canonical dùng chung
    có company_type
-   **recommendation**: v0.1 giữ total_voting_rights_count và áp rule
    theo company_type. \## total_voting_rights_count
-   **item_id**: NC-008
-   **related_field**: total_voting_rights_count
-   **issue**: Một canonical đang bao phủ hai công thức theo loại hình.
-   **current_understanding**: Rulebook áp company_type để chọn công
    thức.
-   **options**: Tách thành total_voting_ballots_tnhh và
    total_votes_present; giữ field chung.
-   **recommendation**: Khi xây Rulebook v1.0 nên tách canonical hoặc
    thêm discriminator company_type. \## director_name
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
