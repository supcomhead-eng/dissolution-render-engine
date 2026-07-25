# FIELD_DICTIONARY_DIFY_v0.1

------------------------------------------------------------------------

# Field: authorized_person_contact_address

## Canonical Field

authorized_person_contact_address

## Domain

person_authorized

## Description

Địa chỉ liên lạc người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID/profile hoặc USER_INPUT

## Validation

Không rỗng

## Required

Có điều kiện

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_date_of_birth

## Canonical Field

authorized_person_date_of_birth

## Domain

person_authorized

## Description

Ngày sinh người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID hoặc profile

## Validation

Ngày hợp lệ

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_email

## Canonical Field

authorized_person_email

## Domain

person_authorized

## Description

Email người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

Profile người được ủy quyền hoặc USER_INPUT

## Validation

Định dạng email

## Required

Có điều kiện

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_gender

## Canonical Field

authorized_person_gender

## Domain

person_authorized

## Description

Giới tính người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID hoặc profile

## Validation

Nam/Nữ

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_id_expiry_date

## Canonical Field

authorized_person_id_expiry_date

## Domain

person_authorized

## Description

Ngày hết hạn CCCD người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID hoặc profile

## Validation

Ngày hợp lệ; sau ngày cấp

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_id_issue_date

## Canonical Field

authorized_person_id_issue_date

## Domain

person_authorized

## Description

Ngày cấp CCCD người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID hoặc profile

## Validation

Ngày hợp lệ

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_id_issue_place

## Canonical Field

authorized_person_id_issue_place

## Domain

person_authorized

## Description

Nơi cấp CCCD người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID hoặc profile

## Validation

Không rỗng

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_id_number

## Canonical Field

authorized_person_id_number

## Domain

person_authorized

## Description

Số CCCD người được ủy quyền/giới thiệu

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID hoặc profile

## Validation

12 chữ số; giữ số 0 đầu

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_job_title

## Canonical Field

authorized_person_job_title

## Domain

person_authorized

## Description

Chức vụ/nghề nghiệp người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

Profile hoặc USER_INPUT

## Validation

Không rỗng

## Required

Có điều kiện

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_name

## Canonical Field

authorized_person_name

## Domain

person_authorized

## Description

Họ tên người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID hoặc hồ sơ profile người được ủy quyền

## Validation

Khớp CCCD

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: authorized_person_phone

## Canonical Field

authorized_person_phone

## Domain

person_authorized

## Description

Số điện thoại người được ủy quyền

## Source Type

DOCUMENT

## Source Detail

Profile người được ủy quyền hoặc USER_INPUT

## Validation

Số điện thoại hợp lệ

## Required

Có điều kiện

## AI Guess

Không

------------------------------------------------------------------------

# Field: board_chairperson_name

## Canonical Field

board_chairperson_name

## Domain

governance

## Description

Tên Chủ tịch Hội đồng quản trị

## Source Type

DOCUMENT

## Source Detail

GPKD/điều lệ/quyết định bổ nhiệm/danh sách cổ đông

## Validation

Không rỗng; đúng người ký

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: business_registration_authority

## Canonical Field

business_registration_authority

## Domain

authority

## Description

Cơ quan đăng ký kinh doanh hiện hành

## Source Type

SEARCH

## Source Detail

Tra theo địa chỉ trụ sở

## Depends On

registered_office_address

## Search Strategy

Ưu tiên Cổng thông tin quốc gia về đăng ký doanh nghiệp và trang chính
thức của tỉnh/Sở Tài chính; đối chiếu địa giới mới nhất

## Validation

Đúng tỉnh/thành và đúng tên cơ quan hiện hành

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: charter_capital_amount

## Canonical Field

charter_capital_amount

## Domain

capital

## Description

Tổng vốn điều lệ bằng số

## Source Type

DOCUMENT

## Source Detail

GPKD

## Validation

Số \>= 0; định dạng dấu phân tách hàng nghìn

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: charter_capital_amount_words

## Canonical Field

charter_capital_amount_words

## Domain

capital

## Description

Tổng vốn điều lệ bằng chữ

## Source Type

RULE

## Source Detail

Sinh từ charter_capital_amount

## Depends On

charter_capital_amount

## Rule

Chuyển số tiền sang chữ tiếng Việt; giữ đơn vị đồng

## Validation

Khớp số tiền

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: company_abbreviation

## Canonical Field

company_abbreviation

## Domain

company

## Description

Tên viết tắt của doanh nghiệp

## Source Type

DOCUMENT

## Source Detail

GPKD; nếu GPKD không ghi thì USER_INPUT

## Validation

Không chứa ký tự đường dẫn

## Required

Có điều kiện

## AI Guess

Không

## Notes

Không tự tạo viết tắt khi giấy tờ và người dùng chưa cung cấp.

------------------------------------------------------------------------

# Field: company_name

## Canonical Field

company_name

## Domain

company

## Description

Tên đầy đủ của doanh nghiệp

## Source Type

DOCUMENT

## Source Detail

Giấy chứng nhận đăng ký doanh nghiệp (GPKD)

## Validation

Không rỗng; đối chiếu cùng MST

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: customs_authority

## Canonical Field

customs_authority

## Domain

authority

## Description

Cơ quan hải quan tiếp nhận/xác nhận nghĩa vụ XNK

## Source Type

SEARCH

## Source Detail

Tra theo địa chỉ trụ sở và tình trạng XNK

## Depends On

registered_office_address, enterprise_tax_code

## Search Strategy

Ưu tiên website Tổng cục Hải quan/Cục Hải quan khu vực; nếu chưa phát
sinh XNK áp dụng cơ quan khu vực quản lý doanh nghiệp

## Validation

Tên cơ quan hiện hành; đúng khu vực

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: director_name

## Canonical Field

director_name

## Domain

person_legal_representative

## Description

Tên Giám đốc dùng tại khối ký/ủy quyền

## Source Type

COMPOSITE

## Source Detail

GPKD và cấu trúc master

## Depends On

legal_representative_name, legal_representative_title

## Rule

Thông thường map tới người đại diện theo pháp luật; nếu người ký không
phải NĐDPL thì cần USER_INPUT

## Validation

Khớp người ký thực tế

## Required

Có

## AI Guess

Không

## Notes

Alias có điều kiện với legal_representative_name.

------------------------------------------------------------------------

# Field: document_year

## Canonical Field

document_year

## Domain

document

## Description

Năm của hồ sơ/văn bản

## Source Type

SYSTEM

## Source Detail

Ngày hệ thống hoặc năm do người dùng chốt

## Validation

4 chữ số

## Required

Có

## AI Guess

Không

## Notes

Các ngày/tháng có thể để trống theo yêu cầu; chỉ điền năm.

------------------------------------------------------------------------

# Field: employee_count

## Canonical Field

employee_count

## Domain

labor

## Description

Số lượng người lao động tại thời điểm giải thể

## Source Type

CONSTANT

## Source Detail

Mặc định theo workflow

## Rule

Mặc định 0, trừ khi hồ sơ thực tế thể hiện khác

## Validation

Số nguyên \>= 0

## Required

Có

## AI Guess

Không

## Notes

Ngoại lệ: phải lấy dữ liệu thực tế nếu doanh nghiệp còn lao động.

------------------------------------------------------------------------

# Field: enterprise_registration_date

## Canonical Field

enterprise_registration_date

## Domain

company

## Description

Ngày đăng ký doanh nghiệp/ngày cấp GPKD

## Source Type

DOCUMENT

## Source Detail

GPKD

## Validation

Ngày hợp lệ dd/mm/yyyy

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: enterprise_tax_code

## Canonical Field

enterprise_tax_code

## Domain

company

## Description

Mã số doanh nghiệp/mã số thuế

## Source Type

DOCUMENT

## Source Detail

GPKD hoặc thông báo mã số thuế

## Validation

Thường 10 hoặc 13 chữ số; giữ số 0 đầu

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: first_member_name

## Canonical Field

first_member_name

## Domain

member

## Description

Tên thành viên thứ nhất/chủ tọa theo master

## Source Type

RULE

## Source Detail

Danh sách thành viên đã sắp thứ tự

## Depends On

member_list

## Rule

Lấy phần tử thứ nhất; cần bảo đảm thứ tự danh sách phản ánh Chủ tịch
HĐTV

## Validation

Có trong danh sách thành viên

## Required

Có

## AI Guess

Không

## Notes

Có thể không đồng nhất với Chủ tịch HĐTV nếu danh sách không được sắp
đúng.

------------------------------------------------------------------------

# Field: generic_email

## Canonical Field

generic_email

## Domain

contact

## Description

Email dùng theo ngữ cảnh

## Source Type

COMPOSITE

## Source Detail

Profile người được giới thiệu/người ủy quyền

## Rule

Xác định vai trò theo master

## Validation

Định dạng email

## Required

Có

## AI Guess

Không

## Notes

Placeholder dùng chung.

------------------------------------------------------------------------

# Field: generic_person_name

## Canonical Field

generic_person_name

## Domain

person

## Description

Tên người dùng theo ngữ cảnh/meta profile

## Source Type

COMPOSITE

## Source Detail

Profile hoặc USER_INPUT

## Rule

CẦN XÁC NHẬN theo vị trí placeholder

## Required

Có điều kiện

## AI Guess

Không

## Notes

Placeholder \[TÊN\] xuất hiện trong hướng dẫn profile, có thể là marker
meta.

------------------------------------------------------------------------

# Field: generic_phone_number

## Canonical Field

generic_phone_number

## Domain

contact

## Description

Số điện thoại dùng theo ngữ cảnh

## Source Type

COMPOSITE

## Source Detail

Profile người được giới thiệu/người ủy quyền hoặc dữ liệu liên hệ doanh
nghiệp

## Rule

Xác định vai trò theo master; trong giấy giới thiệu hiện tại thường là
người được giới thiệu

## Validation

Số điện thoại hợp lệ

## Required

Có

## AI Guess

Không

## Notes

Placeholder dùng chung, dễ nhầm nguồn.

------------------------------------------------------------------------

# Field: legal_representative_date_of_birth

## Canonical Field

legal_representative_date_of_birth

## Domain

person_legal_representative

## Description

Ngày sinh người đại diện

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID

## Validation

Ngày hợp lệ

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: legal_representative_email

## Canonical Field

legal_representative_email

## Domain

person_legal_representative

## Description

Email người đại diện

## Source Type

USER_INPUT

## Source Detail

Người dùng hoặc hồ sơ liên hệ

## Validation

Định dạng email

## Required

Có điều kiện

## AI Guess

Không

------------------------------------------------------------------------

# Field: legal_representative_gender

## Canonical Field

legal_representative_gender

## Domain

person_legal_representative

## Description

Giới tính người đại diện

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID; có thể đối chiếu GPKD

## Validation

Nam/Nữ

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: legal_representative_id_number

## Canonical Field

legal_representative_id_number

## Domain

person_legal_representative

## Description

Số CCCD của người đại diện

## Source Type

DOCUMENT

## Source Detail

CCCD/VNeID

## Validation

12 chữ số; giữ số 0 đầu

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: legal_representative_name

## Canonical Field

legal_representative_name

## Domain

person_legal_representative

## Description

Họ tên người đại diện theo pháp luật

## Source Type

DOCUMENT

## Source Detail

GPKD; đối chiếu CCCD/VNeID

## Rule

Nếu CCCD/VNeID khác GPKD về dữ liệu nhân thân thì ưu tiên CCCD/VNeID

## Validation

Không rỗng; viết hoa theo master khi cần

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: legal_representative_phone

## Canonical Field

legal_representative_phone

## Domain

person_legal_representative

## Description

Số điện thoại người đại diện

## Source Type

USER_INPUT

## Source Detail

Người dùng hoặc hồ sơ liên hệ

## Validation

Chuỗi số điện thoại hợp lệ

## Required

Có điều kiện

## AI Guess

Không

------------------------------------------------------------------------

# Field: legal_representative_title

## Canonical Field

legal_representative_title

## Domain

person_legal_representative

## Description

Chức danh người đại diện theo pháp luật

## Source Type

DOCUMENT

## Source Detail

GPKD

## Validation

Khớp chức danh trên GPKD

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_block_begin_marker

## Canonical Field

member_block_begin_marker

## Domain

template_control

## Description

Điểm bắt đầu block lặp thành viên

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Không fill dữ liệu; dùng để điều khiển expand block

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_block_end_marker

## Canonical Field

member_block_end_marker

## Domain

template_control

## Description

Điểm kết thúc block lặp thành viên

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Không fill dữ liệu; xóa marker sau khi expand

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_capital_amount

## Canonical Field

member_capital_amount

## Domain

member

## Description

Giá trị vốn góp của thành viên

## Source Type

DOCUMENT

## Source Detail

GPKD/danh sách thành viên

## Validation

Số \>= 0; tổng bằng vốn điều lệ

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_capital_amount_words

## Canonical Field

member_capital_amount_words

## Domain

member

## Description

Vốn góp bằng chữ

## Source Type

RULE

## Source Detail

Sinh từ member_capital_amount

## Depends On

member_capital_amount

## Rule

Chuyển số tiền sang chữ tiếng Việt

## Validation

Khớp vốn góp bằng số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_capital_ratio

## Canonical Field

member_capital_ratio

## Domain

member

## Description

Tỷ lệ vốn góp của thành viên

## Source Type

RULE

## Source Detail

GPKD hoặc tính từ vốn góp

## Depends On

member_capital_amount, charter_capital_amount

## Rule

Ưu tiên tỷ lệ trên giấy tờ; nếu thiếu: vốn góp/tổng vốn × 100

## Validation

0--100%; tổng danh sách = 100%

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_council_chairperson_name

## Canonical Field

member_council_chairperson_name

## Domain

governance

## Description

Tên Chủ tịch Hội đồng thành viên

## Source Type

DOCUMENT

## Source Detail

GPKD, điều lệ, biên bản/quyết định nội bộ

## Validation

Có trong danh sách thành viên

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_name

## Canonical Field

member_name

## Domain

member

## Description

Họ tên thành viên góp vốn

## Source Type

DOCUMENT

## Source Detail

GPKD/danh sách thành viên

## Validation

Không rỗng; số lượng khớp danh sách

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: member_sequence_number

## Canonical Field

member_sequence_number

## Domain

member

## Description

Số thứ tự thành viên

## Source Type

RULE

## Source Detail

Vị trí trong danh sách

## Depends On

member_list

## Rule

Đánh số bắt đầu từ 1

## Validation

Số nguyên dương

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: owner_name

## Canonical Field

owner_name

## Domain

ownership

## Description

Tên chủ sở hữu công ty TNHH một thành viên

## Source Type

DOCUMENT

## Source Detail

GPKD/CCCD/VNeID

## Validation

Khớp chủ sở hữu trên GPKD

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: person_honorific

## Canonical Field

person_honorific

## Domain

person

## Description

Danh xưng Ông/Bà

## Source Type

RULE

## Source Detail

Suy từ giới tính của người tại đúng ngữ cảnh

## Depends On

person_gender

## Rule

Nam → Ông; Nữ → Bà

## Validation

Chỉ Ông hoặc Bà

## Required

Có

## AI Guess

Không

## Notes

Placeholder dùng chung nhiều vai trò; xác định người phụ thuộc theo vị
trí trong master.

------------------------------------------------------------------------

# Field: present_member_block_begin_marker

## Canonical Field

present_member_block_begin_marker

## Domain

template_control

## Description

Điểm bắt đầu block thành viên có mặt

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Expand từ danh sách thành viên có mặt; workflow thường mặc định tất cả
có mặt

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: present_member_block_end_marker

## Canonical Field

present_member_block_end_marker

## Domain

template_control

## Description

Điểm kết thúc block thành viên có mặt

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Xóa marker sau khi expand

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: present_shareholder_block_begin_marker

## Canonical Field

present_shareholder_block_begin_marker

## Domain

template_control

## Description

Điểm bắt đầu block cổ đông có mặt (phiên bản cũ)

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Expand danh sách cổ đông có mặt; phiên bản mới đã đổi sang BEGIN_CO_DONG

## Required

Có

## AI Guess

Không

## Notes

Alias/phiên bản cũ, chưa tự gộp marker.

------------------------------------------------------------------------

# Field: present_shareholder_block_end_marker

## Canonical Field

present_shareholder_block_end_marker

## Domain

template_control

## Description

Điểm kết thúc block cổ đông có mặt (phiên bản cũ)

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Xóa marker sau khi expand

## Required

Có

## AI Guess

Không

## Notes

Alias/phiên bản cũ, chưa tự gộp marker.

------------------------------------------------------------------------

# Field: registered_office_address

## Canonical Field

registered_office_address

## Domain

company

## Description

Địa chỉ trụ sở chính

## Source Type

DOCUMENT

## Source Detail

GPKD

## Validation

Không rỗng; dùng đúng địa chỉ trên giấy tờ, đồng thời lưu bản chuẩn hóa
địa giới nếu có

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: share_par_value

## Canonical Field

share_par_value

## Domain

shareholder

## Description

Mệnh giá một cổ phần

## Source Type

CONSTANT

## Source Detail

Quy ước workflow CTCP

## Rule

Mặc định 10.000 đồng/cổ phần

## Validation

10.000, trừ khi giấy tờ thể hiện khác

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_block_begin_marker

## Canonical Field

shareholder_block_begin_marker

## Domain

template_control

## Description

Điểm bắt đầu block lặp cổ đông

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Expand tất cả occurrence từ cùng danh sách cổ đông

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_block_end_marker

## Canonical Field

shareholder_block_end_marker

## Domain

template_control

## Description

Điểm kết thúc block lặp cổ đông

## Source Type

CONSTANT

## Source Detail

Master Word

## Rule

Xóa marker sau khi expand

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_contributed_capital_value

## Canonical Field

shareholder_contributed_capital_value

## Domain

shareholder

## Description

Giá trị vốn góp của cổ đông

## Source Type

RULE

## Source Detail

Số cổ phần và mệnh giá

## Depends On

shareholder_share_count, share_par_value

## Rule

Giá trị vốn góp = số cổ phần × mệnh giá

## Validation

Tổng bằng vốn điều lệ

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_name

## Canonical Field

shareholder_name

## Domain

shareholder

## Description

Họ tên cổ đông

## Source Type

DOCUMENT

## Source Detail

Danh sách cổ đông/GPKD và CCCD

## Validation

Không rỗng; khớp danh sách cổ đông

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_ownership_percentage

## Canonical Field

shareholder_ownership_percentage

## Domain

shareholder

## Description

Tỷ lệ sở hữu cổ phần

## Source Type

RULE

## Source Detail

Danh sách cổ đông hoặc tính toán

## Depends On

shareholder_share_count, total_share_count

## Rule

Ưu tiên giấy tờ; nếu thiếu: số cổ phần/tổng cổ phần × 100

## Validation

0--100%; tổng = 100%

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_sequence_number

## Canonical Field

shareholder_sequence_number

## Domain

shareholder

## Description

Số thứ tự cổ đông

## Source Type

RULE

## Source Detail

Vị trí trong danh sách cổ đông

## Depends On

shareholder_list

## Rule

Đánh số bắt đầu từ 1

## Validation

Số nguyên dương

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_share_count

## Canonical Field

shareholder_share_count

## Domain

shareholder

## Description

Số cổ phần sở hữu

## Source Type

DOCUMENT

## Source Detail

Danh sách cổ đông

## Validation

Số nguyên \>= 0; tổng khớp tổng số cổ phần

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_share_type

## Canonical Field

shareholder_share_type

## Domain

shareholder

## Description

Loại cổ phần

## Source Type

CONSTANT

## Source Detail

Mặc định theo workflow; đối chiếu danh sách cổ đông

## Rule

Mặc định 'Phổ thông' nếu không có loại khác

## Validation

Giá trị hợp lệ theo hồ sơ

## Required

Có

## AI Guess

Không

## Notes

Ngoại lệ: cổ phần ưu đãi hoặc loại khác phải đọc từ giấy tờ.

------------------------------------------------------------------------

# Field: shareholder_share_value

## Canonical Field

shareholder_share_value

## Domain

shareholder

## Description

Giá trị cổ phần/giá trị hoàn trả trong master thanh lý

## Source Type

RULE

## Source Detail

Số cổ phần và mệnh giá

## Depends On

shareholder_share_count, share_par_value

## Rule

Theo workflow hiện tại: giá trị cổ phần = giá trị hoàn trả = số cổ phần
× 10.000

## Validation

Khớp tỷ lệ và tổng giá trị

## Required

Có

## AI Guess

Không

## Notes

Ngoại lệ nghiệp vụ có thể khác; v0.1 giữ cách hiểu đã chốt.

------------------------------------------------------------------------

# Field: shareholder_share_value_words

## Canonical Field

shareholder_share_value_words

## Domain

shareholder

## Description

Giá trị cổ phần bằng chữ

## Source Type

RULE

## Source Detail

Sinh từ shareholder_share_value

## Depends On

shareholder_share_value

## Rule

Chuyển số tiền sang chữ tiếng Việt

## Validation

Khớp giá trị bằng số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: shareholder_vote_count

## Canonical Field

shareholder_vote_count

## Domain

voting

## Description

Số phiếu biểu quyết của cổ đông

## Source Type

RULE

## Source Detail

Số cổ phần có quyền biểu quyết

## Depends On

shareholder_share_count

## Rule

Đối với cổ phần phổ thông: số phiếu = số cổ phần

## Validation

Số nguyên \>= 0

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: signing_place

## Canonical Field

signing_place

## Domain

document

## Description

Địa danh ghi tại phần ngày ký

## Source Type

RULE

## Source Detail

Suy từ địa chỉ trụ sở và địa giới hiện hành

## Depends On

registered_office_address

## Rule

Ưu tiên tỉnh/thành phố hiện hành nơi doanh nghiệp đặt trụ sở

## Validation

Phù hợp địa giới hành chính hiện hành

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_authority

## Canonical Field

tax_authority

## Domain

authority

## Description

Cơ quan thuế quản lý trực tiếp

## Source Type

SEARCH

## Source Detail

Tra theo địa chỉ trụ sở và MST

## Depends On

registered_office_address, enterprise_tax_code

## Search Strategy

Ưu tiên cổng/website chính thức của cơ quan thuế và thông tin quản lý
MST

## Validation

Khớp địa bàn, MST và cơ quan quản lý hiện hành

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_1

## Canonical Field

tax_code_digit_1

## Domain

tax

## Description

Chữ số thứ 1 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 1

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_10

## Canonical Field

tax_code_digit_10

## Domain

tax

## Description

Chữ số thứ 10 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 10

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_2

## Canonical Field

tax_code_digit_2

## Domain

tax

## Description

Chữ số thứ 2 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 2

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_3

## Canonical Field

tax_code_digit_3

## Domain

tax

## Description

Chữ số thứ 3 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 3

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_4

## Canonical Field

tax_code_digit_4

## Domain

tax

## Description

Chữ số thứ 4 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 4

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_5

## Canonical Field

tax_code_digit_5

## Domain

tax

## Description

Chữ số thứ 5 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 5

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_6

## Canonical Field

tax_code_digit_6

## Domain

tax

## Description

Chữ số thứ 6 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 6

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_7

## Canonical Field

tax_code_digit_7

## Domain

tax

## Description

Chữ số thứ 7 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 7

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_8

## Canonical Field

tax_code_digit_8

## Domain

tax

## Description

Chữ số thứ 8 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 8

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_code_digit_9

## Canonical Field

tax_code_digit_9

## Domain

tax

## Description

Chữ số thứ 9 của MST

## Source Type

RULE

## Source Detail

Tách từ enterprise_tax_code

## Depends On

enterprise_tax_code

## Rule

Một placeholder = một ký tự, index 9

## Validation

Một chữ số

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: tax_form_item_label_01

## Canonical Field

tax_form_item_label_01

## Domain

template_control

## Description

Nhãn chỉ tiêu cố định \[01\] trong biểu mẫu thuế

## Source Type

CONSTANT

## Source Detail

Nội dung biểu mẫu pháp định

## Rule

Không thay thế; giữ nguyên nhãn mẫu

## Validation

Giữ nguyên \[01\]

## Required

Không

## AI Guess

Không

## Notes

Được regex nhận diện vì có ngoặc vuông nhưng có khả năng không phải
placeholder.

------------------------------------------------------------------------

# Field: tax_form_item_label_02

## Canonical Field

tax_form_item_label_02

## Domain

template_control

## Description

Nhãn chỉ tiêu cố định \[02\] trong biểu mẫu thuế

## Source Type

CONSTANT

## Source Detail

Nội dung biểu mẫu pháp định

## Rule

Không thay thế; giữ nguyên nhãn mẫu

## Validation

Giữ nguyên \[02\]

## Required

Không

## AI Guess

Không

## Notes

Được regex nhận diện vì có ngoặc vuông nhưng có khả năng không phải
placeholder.

------------------------------------------------------------------------

# Field: tax_form_item_label_03

## Canonical Field

tax_form_item_label_03

## Domain

template_control

## Description

Nhãn chỉ tiêu cố định \[03\] trong biểu mẫu thuế

## Source Type

CONSTANT

## Source Detail

Nội dung biểu mẫu pháp định

## Rule

Không thay thế; giữ nguyên nhãn mẫu

## Validation

Giữ nguyên \[03\]

## Required

Không

## AI Guess

Không

## Notes

Được regex nhận diện vì có ngoặc vuông nhưng có khả năng không phải
placeholder.

------------------------------------------------------------------------

# Field: tax_form_item_label_04

## Canonical Field

tax_form_item_label_04

## Domain

template_control

## Description

Nhãn chỉ tiêu cố định \[04\] trong biểu mẫu thuế

## Source Type

CONSTANT

## Source Detail

Nội dung biểu mẫu pháp định

## Rule

Không thay thế; giữ nguyên nhãn mẫu

## Validation

Giữ nguyên \[04\]

## Required

Không

## AI Guess

Không

## Notes

Được regex nhận diện vì có ngoặc vuông nhưng có khả năng không phải
placeholder.

------------------------------------------------------------------------

# Field: tax_form_item_label_05

## Canonical Field

tax_form_item_label_05

## Domain

template_control

## Description

Nhãn chỉ tiêu cố định \[05\] trong biểu mẫu thuế

## Source Type

CONSTANT

## Source Detail

Nội dung biểu mẫu pháp định

## Rule

Không thay thế; giữ nguyên nhãn mẫu

## Validation

Giữ nguyên \[05\]

## Required

Không

## AI Guess

Không

## Notes

Được regex nhận diện vì có ngoặc vuông nhưng có khả năng không phải
placeholder.

------------------------------------------------------------------------

# Field: total_member_count

## Canonical Field

total_member_count

## Domain

member

## Description

Tổng số thành viên

## Source Type

RULE

## Source Detail

Đếm danh sách thành viên

## Depends On

member_list

## Rule

Đếm số bản ghi hợp lệ

## Validation

Số nguyên \>= 2 đối với TNHH 2TV+

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_refund_value

## Canonical Field

total_refund_value

## Domain

liquidation

## Description

Tổng giá trị hoàn trả cho cổ đông

## Source Type

RULE

## Source Detail

Theo workflow hiện tại bằng tổng tài sản còn lại

## Depends On

total_remaining_asset_value

## Rule

Mặc định total_refund_value = total_remaining_asset_value

## Validation

Tổng chi tiết hoàn trả = tổng hoàn trả

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_refund_value_words

## Canonical Field

total_refund_value_words

## Domain

liquidation

## Description

Tổng hoàn trả bằng chữ

## Source Type

RULE

## Source Detail

Sinh từ total_refund_value

## Depends On

total_refund_value

## Rule

Chuyển số tiền sang chữ tiếng Việt

## Validation

Khớp số tiền

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_remaining_asset_value

## Canonical Field

total_remaining_asset_value

## Domain

liquidation

## Description

Tổng giá trị tài sản còn lại

## Source Type

USER_INPUT

## Source Detail

Sổ sách/biên bản thanh lý hoặc người dùng cung cấp

## Validation

Số \>= 0; định dạng nghìn

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_remaining_asset_value_words

## Canonical Field

total_remaining_asset_value_words

## Domain

liquidation

## Description

Tổng tài sản còn lại bằng chữ

## Source Type

RULE

## Source Detail

Sinh từ total_remaining_asset_value

## Depends On

total_remaining_asset_value

## Rule

Chuyển số tiền sang chữ tiếng Việt

## Validation

Khớp số tiền

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_share_count

## Canonical Field

total_share_count

## Domain

shareholder

## Description

Tổng số cổ phần

## Source Type

RULE

## Source Detail

Cộng số cổ phần của các cổ đông

## Depends On

shareholder_list

## Rule

Tổng shareholder_share_count

## Validation

Khớp GPKD và vốn điều lệ/mệnh giá

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_shareholder_count

## Canonical Field

total_shareholder_count

## Domain

shareholder

## Description

Tổng số cổ đông tham gia/danh sách

## Source Type

RULE

## Source Detail

Đếm danh sách cổ đông

## Depends On

shareholder_list

## Rule

Đếm số bản ghi cổ đông hợp lệ

## Validation

Số nguyên \> 0

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_votes_present

## Canonical Field

total_votes_present

## Domain

voting

## Description

Tổng số phiếu của cổ đông dự họp

## Source Type

RULE

## Source Detail

Cộng phiếu cổ đông dự họp

## Depends On

shareholder_vote_count

## Rule

Bằng tổng số cổ phần có quyền biểu quyết của cổ đông dự họp; trong
workflow hiện tại đạt 100%

## Validation

Số nguyên; khớp tổng cổ phần dự họp

## Required

Có

## AI Guess

Không

------------------------------------------------------------------------

# Field: total_voting_rights_count

## Canonical Field

total_voting_rights_count

## Domain

voting

## Description

Tổng số phiếu biểu quyết (placeholder cũ/dùng chung)

## Source Type

RULE

## Source Detail

Phụ thuộc loại hình

## Depends On

company_type, charter_capital_amount, total_share_count

## Rule

TNHH: vốn điều lệ/10.000; CTCP: tổng cổ phần có quyền biểu quyết

## Validation

Số nguyên; định dạng nghìn

## Required

Có

## AI Guess

Không

## Notes

Có nhiều cách hiểu theo master; cần xác nhận khi dùng ngoài ngữ cảnh.

# NEEDS_CONFIRMATION

## generic_phone_number

-   **master_id**: MASTER_001
-   **placeholder_original**: \[SỐ ĐIỆN THOẠI\]
-   **proposed_canonical_field**: generic_phone_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Có thể là số người được giới thiệu hoặc số liên hệ doanh
    nghiệp.
-   **options**: authorized_person_phone; company_contact_phone
-   **recommendation**: Xác định theo master trước khi fill.

## person_honorific

-   **master_id**: MASTER_003
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## person_honorific

-   **master_id**: MASTER_004
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## present_shareholder_block_begin_marker

-   **master_id**: MASTER_005
-   **placeholder_original**: \[BEGIN_CO_DONG_CO_MAT\]
-   **proposed_canonical_field**: present_shareholder_block_begin_marker
-   **issue_type**: LEGACY_ALIAS
-   **reason**: Marker cũ đã được đổi thành BEGIN_CO_DONG ở master chốt
    sau.
-   **options**: Giữ marker riêng; alias với shareholder block
-   **recommendation**: Không tự thay master; mapping riêng và ghi phiên
    bản cũ.

## present_shareholder_block_end_marker

-   **master_id**: MASTER_005
-   **placeholder_original**: \[END_CO_DONG_CO_MAT\]
-   **proposed_canonical_field**: present_shareholder_block_end_marker
-   **issue_type**: LEGACY_ALIAS
-   **reason**: Marker cũ đã được đổi thành END_CO_DONG ở master chốt
    sau.
-   **options**: Giữ marker riêng; alias với shareholder block
-   **recommendation**: Không tự thay master; mapping riêng và ghi phiên
    bản cũ.

## shareholder_sequence_number

-   **master_id**: MASTER_005
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## total_voting_rights_count

-   **master_id**: MASTER_005
-   **placeholder_original**: \[TỔNG SỐ PHIẾU BIỂU QUYẾT\]
-   **proposed_canonical_field**: total_voting_rights_count
-   **issue_type**: MULTIPLE_RULES
-   **reason**: TNHH dùng vốn điều lệ/10.000; CTCP dùng tổng cổ phần có
    quyền biểu quyết.
-   **options**: Tách canonical theo loại hình; giữ canonical dùng chung
    có company_type
-   **recommendation**: v0.1 giữ total_voting_rights_count và áp rule
    theo company_type.

## person_honorific

-   **master_id**: MASTER_005
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## shareholder_sequence_number

-   **master_id**: MASTER_006
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## total_voting_rights_count

-   **master_id**: MASTER_006
-   **placeholder_original**: \[TỔNG SỐ PHIẾU BIỂU QUYẾT\]
-   **proposed_canonical_field**: total_voting_rights_count
-   **issue_type**: MULTIPLE_RULES
-   **reason**: TNHH dùng vốn điều lệ/10.000; CTCP dùng tổng cổ phần có
    quyền biểu quyết.
-   **options**: Tách canonical theo loại hình; giữ canonical dùng chung
    có company_type
-   **recommendation**: v0.1 giữ total_voting_rights_count và áp rule
    theo company_type.

## person_honorific

-   **master_id**: MASTER_006
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## shareholder_sequence_number

-   **master_id**: MASTER_007
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## person_honorific

-   **master_id**: MASTER_007
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## tax_form_item_label_01

-   **master_id**: MASTER_009
-   **placeholder_original**: \[01\]
-   **proposed_canonical_field**: tax_form_item_label_01
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_02

-   **master_id**: MASTER_009
-   **placeholder_original**: \[02\]
-   **proposed_canonical_field**: tax_form_item_label_02
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_03

-   **master_id**: MASTER_009
-   **placeholder_original**: \[03\]
-   **proposed_canonical_field**: tax_form_item_label_03
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_04

-   **master_id**: MASTER_009
-   **placeholder_original**: \[04\]
-   **proposed_canonical_field**: tax_form_item_label_04
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_05

-   **master_id**: MASTER_009
-   **placeholder_original**: \[05\]
-   **proposed_canonical_field**: tax_form_item_label_05
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_01

-   **master_id**: MASTER_010
-   **placeholder_original**: \[01\]
-   **proposed_canonical_field**: tax_form_item_label_01
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_02

-   **master_id**: MASTER_010
-   **placeholder_original**: \[02\]
-   **proposed_canonical_field**: tax_form_item_label_02
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_03

-   **master_id**: MASTER_010
-   **placeholder_original**: \[03\]
-   **proposed_canonical_field**: tax_form_item_label_03
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_04

-   **master_id**: MASTER_010
-   **placeholder_original**: \[04\]
-   **proposed_canonical_field**: tax_form_item_label_04
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## tax_form_item_label_05

-   **master_id**: MASTER_010
-   **placeholder_original**: \[05\]
-   **proposed_canonical_field**: tax_form_item_label_05
-   **issue_type**: NOT_DATA_PLACEHOLDER
-   **reason**: Đây nhiều khả năng là số chỉ tiêu cố định của mẫu thuế,
    không phải field cần replace.
-   **options**: Giữ nguyên constant; loại khỏi replace scan
-   **recommendation**: Đưa vào canonical template_control và cấm
    replace.

## person_honorific

-   **master_id**: MASTER_011
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## person_honorific

-   **master_id**: MASTER_012
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## person_honorific

-   **master_id**: MASTER_013
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## shareholder_share_value

-   **master_id**: MASTER_016
-   **placeholder_original**: \[GIÁ TRỊ CỔ PHẦN\]
-   **proposed_canonical_field**: shareholder_share_value
-   **issue_type**: BUSINESS_RULE_EXCEPTION
-   **reason**: Trong bộ hồ sơ hiện tại được chốt bằng giá trị hoàn trả,
    nhưng thực tế có thể khác nếu tài sản còn lại khác vốn góp.
-   **options**: shareholder_share_value; shareholder_refund_value
-   **recommendation**: v0.1 giữ một canonical theo rule đã chốt; tách ở
    phiên bản sau nếu phát sinh ngoại lệ.

## shareholder_sequence_number

-   **master_id**: MASTER_016
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## shareholder_share_value

-   **master_id**: MASTER_017
-   **placeholder_original**: \[GIÁ TRỊ CỔ PHẦN\]
-   **proposed_canonical_field**: shareholder_share_value
-   **issue_type**: BUSINESS_RULE_EXCEPTION
-   **reason**: Trong bộ hồ sơ hiện tại được chốt bằng giá trị hoàn trả,
    nhưng thực tế có thể khác nếu tài sản còn lại khác vốn góp.
-   **options**: shareholder_share_value; shareholder_refund_value
-   **recommendation**: v0.1 giữ một canonical theo rule đã chốt; tách ở
    phiên bản sau nếu phát sinh ngoại lệ.

## shareholder_sequence_number

-   **master_id**: MASTER_017
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## shareholder_share_value

-   **master_id**: MASTER_018
-   **placeholder_original**: \[GIÁ TRỊ CỔ PHẦN\]
-   **proposed_canonical_field**: shareholder_share_value
-   **issue_type**: BUSINESS_RULE_EXCEPTION
-   **reason**: Trong bộ hồ sơ hiện tại được chốt bằng giá trị hoàn trả,
    nhưng thực tế có thể khác nếu tài sản còn lại khác vốn góp.
-   **options**: shareholder_share_value; shareholder_refund_value
-   **recommendation**: v0.1 giữ một canonical theo rule đã chốt; tách ở
    phiên bản sau nếu phát sinh ngoại lệ.

## shareholder_sequence_number

-   **master_id**: MASTER_018
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## person_honorific

-   **master_id**: MASTER_021
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## shareholder_sequence_number

-   **master_id**: MASTER_024
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## director_name

-   **master_id**: MASTER_024
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## person_honorific

-   **master_id**: MASTER_024
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## shareholder_sequence_number

-   **master_id**: MASTER_025
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## director_name

-   **master_id**: MASTER_025
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## total_voting_rights_count

-   **master_id**: MASTER_025
-   **placeholder_original**: \[TỔNG SỐ PHIẾU BIỂU QUYẾT\]
-   **proposed_canonical_field**: total_voting_rights_count
-   **issue_type**: MULTIPLE_RULES
-   **reason**: TNHH dùng vốn điều lệ/10.000; CTCP dùng tổng cổ phần có
    quyền biểu quyết.
-   **options**: Tách canonical theo loại hình; giữ canonical dùng chung
    có company_type
-   **recommendation**: v0.1 giữ total_voting_rights_count và áp rule
    theo company_type.

## person_honorific

-   **master_id**: MASTER_025
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## shareholder_sequence_number

-   **master_id**: MASTER_026
-   **placeholder_original**: \[STT\]
-   **proposed_canonical_field**: shareholder_sequence_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Số thứ tự có thể là thành viên hoặc cổ đông.
-   **options**: member_sequence_number; shareholder_sequence_number
-   **recommendation**: Map theo loại master/block; không dùng mapping
    chung ngoài ngữ cảnh.

## director_name

-   **master_id**: MASTER_026
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## total_voting_rights_count

-   **master_id**: MASTER_026
-   **placeholder_original**: \[TỔNG SỐ PHIẾU BIỂU QUYẾT\]
-   **proposed_canonical_field**: total_voting_rights_count
-   **issue_type**: MULTIPLE_RULES
-   **reason**: TNHH dùng vốn điều lệ/10.000; CTCP dùng tổng cổ phần có
    quyền biểu quyết.
-   **options**: Tách canonical theo loại hình; giữ canonical dùng chung
    có company_type
-   **recommendation**: v0.1 giữ total_voting_rights_count và áp rule
    theo company_type.

## person_honorific

-   **master_id**: MASTER_026
-   **placeholder_original**: \[ÔNG/BÀ\]
-   **proposed_canonical_field**: person_honorific
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Cùng placeholder được dùng cho chủ sở hữu, thành viên
    hoặc người đại diện.
-   **options**: Suy theo field giới tính của người ngay sau
    placeholder; tách placeholder theo vai trò
-   **recommendation**: v0.1 giữ person_honorific và bắt buộc engine xác
    định vai trò theo vị trí.

## generic_email

-   **master_id**: MASTER_027
-   **placeholder_original**: \[EMAIL\]
-   **proposed_canonical_field**: generic_email
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Có thể là email người được giới thiệu/người ủy quyền
    hoặc email doanh nghiệp.
-   **options**: authorized_person_email; company_contact_email
-   **recommendation**: Xác định theo master trước khi fill.

## authorized_person_id_issue_date

-   **master_id**: MASTER_027
-   **placeholder_original**: \[NGÀY CẤP CCCD\]
-   **proposed_canonical_field**: authorized_person_id_issue_date
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Placeholder không ghi rõ CCCD của người đại diện hay
    người được ủy quyền.
-   **options**: authorized_person_id_issue_date;
    legal_representative_id_issue_date
-   **recommendation**: Theo các master hiện tại map người được ủy
    quyền/giới thiệu; kiểm tra khi tái sử dụng.

## generic_phone_number

-   **master_id**: MASTER_027
-   **placeholder_original**: \[SỐ ĐIỆN THOẠI\]
-   **proposed_canonical_field**: generic_phone_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Có thể là số người được giới thiệu hoặc số liên hệ doanh
    nghiệp.
-   **options**: authorized_person_phone; company_contact_phone
-   **recommendation**: Xác định theo master trước khi fill.

## authorized_person_id_issue_date

-   **master_id**: MASTER_029
-   **placeholder_original**: \[NGÀY CẤP CCCD\]
-   **proposed_canonical_field**: authorized_person_id_issue_date
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Placeholder không ghi rõ CCCD của người đại diện hay
    người được ủy quyền.
-   **options**: authorized_person_id_issue_date;
    legal_representative_id_issue_date
-   **recommendation**: Theo các master hiện tại map người được ủy
    quyền/giới thiệu; kiểm tra khi tái sử dụng.

## authorized_person_id_issue_place

-   **master_id**: MASTER_029
-   **placeholder_original**: \[NƠI CẤP CCCD\]
-   **proposed_canonical_field**: authorized_person_id_issue_place
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Placeholder không ghi rõ chủ thể.
-   **options**: authorized_person_id_issue_place;
    legal_representative_id_issue_place
-   **recommendation**: Theo master CTCP hiện tại map người được ủy
    quyền.

## director_name

-   **master_id**: MASTER_029
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## director_name

-   **master_id**: MASTER_030
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## director_name

-   **master_id**: MASTER_031
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## authorized_person_id_issue_date

-   **master_id**: MASTER_032
-   **placeholder_original**: \[NGÀY CẤP CCCD\]
-   **proposed_canonical_field**: authorized_person_id_issue_date
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Placeholder không ghi rõ CCCD của người đại diện hay
    người được ủy quyền.
-   **options**: authorized_person_id_issue_date;
    legal_representative_id_issue_date
-   **recommendation**: Theo các master hiện tại map người được ủy
    quyền/giới thiệu; kiểm tra khi tái sử dụng.

## authorized_person_id_issue_place

-   **master_id**: MASTER_032
-   **placeholder_original**: \[NƠI CẤP CCCD\]
-   **proposed_canonical_field**: authorized_person_id_issue_place
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Placeholder không ghi rõ chủ thể.
-   **options**: authorized_person_id_issue_place;
    legal_representative_id_issue_place
-   **recommendation**: Theo master CTCP hiện tại map người được ủy
    quyền.

## director_name

-   **master_id**: MASTER_032
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## director_name

-   **master_id**: MASTER_033
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## director_name

-   **master_id**: MASTER_034
-   **placeholder_original**: \[TÊN GIÁM ĐỐC\]
-   **proposed_canonical_field**: director_name
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Có thể là NĐDPL, nhưng không phải mọi doanh nghiệp đều
    có NĐDPL giữ chức Giám đốc.
-   **options**: legal_representative_name; separate signing_person_name
-   **recommendation**: v0.1 dùng director_name COMPOSITE; cần xác nhận
    khi chức danh không phải Giám đốc.

## generic_email

-   **master_id**: MASTER_035
-   **placeholder_original**: \[EMAIL\]
-   **proposed_canonical_field**: generic_email
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Có thể là email người được giới thiệu/người ủy quyền
    hoặc email doanh nghiệp.
-   **options**: authorized_person_email; company_contact_email
-   **recommendation**: Xác định theo master trước khi fill.

## authorized_person_id_issue_date

-   **master_id**: MASTER_035
-   **placeholder_original**: \[NGÀY CẤP CCCD\]
-   **proposed_canonical_field**: authorized_person_id_issue_date
-   **issue_type**: POSSIBLE_ALIAS
-   **reason**: Placeholder không ghi rõ CCCD của người đại diện hay
    người được ủy quyền.
-   **options**: authorized_person_id_issue_date;
    legal_representative_id_issue_date
-   **recommendation**: Theo các master hiện tại map người được ủy
    quyền/giới thiệu; kiểm tra khi tái sử dụng.

## generic_phone_number

-   **master_id**: MASTER_035
-   **placeholder_original**: \[SỐ ĐIỆN THOẠI\]
-   **proposed_canonical_field**: generic_phone_number
-   **issue_type**: CONTEXT_DEPENDENT
-   **reason**: Có thể là số người được giới thiệu hoặc số liên hệ doanh
    nghiệp.
-   **options**: authorized_person_phone; company_contact_phone
-   **recommendation**: Xác định theo master trước khi fill.

## generic_person_name

-   **master_id**: MASTER_035
-   **placeholder_original**: \[TÊN\]
-   **proposed_canonical_field**: generic_person_name
-   **issue_type**: META_PLACEHOLDER
-   **reason**: Xuất hiện trong câu hướng dẫn thêm block profile, chưa
    xác định có được render hay chỉ là ví dụ.
-   **options**: generic_person_name; không phải field runtime
-   **recommendation**: Không tự fill cho đến khi xác nhận.
