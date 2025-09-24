# 🎓 Flashcard Sinh Viên + AI Tóm Tắt Bài Giảng

Ứng dụng web giúp **sinh viên** và **người học** ôn tập hiệu quả thông qua **flashcard tương tác**.  
Kết hợp AI để **tóm tắt nội dung bài giảng** nhanh chóng, hỗ trợ học tập thông minh và tiết kiệm thời gian.

---

## 🌟 Điểm nổi bật
- 🃏 **Flashcard lật 2 mặt**: hỏi – đáp, hỗ trợ ghi nhớ lâu dài.  
- 🔊 **Đọc to câu hỏi và đáp án** (Text-to-Speech giọng Việt).  
- 🎯 **Câu hỏi trắc nghiệm**: chọn đáp án, hiển thị đúng/sai trực quan.  
- 🖋 **Tóm tắt nội dung bằng AI**: sinh bản tóm tắt ngắn, gạch đầu dòng, hoặc chi tiết.  
- ➕ **Thêm câu hỏi ngẫu nhiên** từ ngân hàng có sẵn.  
- 🗑 **Xóa toàn bộ flashcard** khi cần bắt đầu lại.  
- 📱 **Giao diện responsive**: hoạt động tốt trên desktop & mobile.  

---

## 🖼 Demo giao diện
- **Trang chính**: hiển thị flashcard dạng lưới.  
- **Mặt trước**: câu hỏi + các đáp án lựa chọn.  
- **Mặt sau**: hiển thị đáp án đúng + giải thích.  
- **Modal AI**: nhập nội dung bài giảng, chọn kiểu tóm tắt và nhận kết quả.  

---

## 🔧 Công nghệ sử dụng
- **HTML5 / CSS3 / JavaScript** (thuần).  
- **TailwindCSS**: tạo giao diện đẹp, hiện đại.  
- **SpeechSynthesis API**: đọc văn bản (câu hỏi/đáp án) bằng giọng Việt.  
- **Fetch API**: gửi yêu cầu tới `/api/summarize` để gọi AI sinh tóm tắt.  

---

## 🚀 Cách chạy
1. Lưu code dưới dạng `index.html`.  
2. Mở file bằng trình duyệt (Chrome, Edge, Firefox).  
3. Đảm bảo có server backend xử lý API `POST /api/summarize` (trả về JSON `{ summary: "..." }`).  

---

## 📌 Cách sử dụng
1. **Bắt đầu học**: khi mở trang sẽ có sẵn 3 flashcard.  
2. **Trả lời câu hỏi**: chọn đáp án, hệ thống hiển thị đúng/sai.  
3. **Xem đáp án**: flashcard tự lật ra mặt sau sau khi chọn đúng.  
4. **Nghe câu hỏi/đáp án**: bấm nút 🔊 để hệ thống đọc to.  
5. **Thêm câu hỏi**: nhấn `+ Thêm câu hỏi` để lấy ngẫu nhiên từ ngân hàng.  
6. **Tóm tắt AI**: nhấn `🤖 Tóm tắt bài bằng AI` → nhập nội dung → chọn kiểu → bấm `Tạo tóm tắt`.  
7. **Xóa tất cả**: làm mới toàn bộ flashcard để học lại từ đầu.  

---

## 🧠 Workflow AI
1. Người dùng nhập nội dung bài giảng vào modal.  
2. Hệ thống gửi yêu cầu tới API `/api/summarize` với:  
   ```json
   { "text": "nội dung...", "style": "short | bullets | detailed" }

## Cấu trúc code
index.html

 ├─ <style>  # CSS cho flip card, modal, button, responsive
 
 ├─ <header> # Thanh điều hướng (thêm câu hỏi, gọi AI, xóa tất cả)
 
 ├─ <main>   # Khu vực hiển thị flashcards
 
 ├─ <div>    # Modal AI (nhập bài giảng, nhận tóm tắt)
 
 └─ <script> # Xử lý flashcard, giọng nói, gọi API, logic học tập
 
## Hướng phát triển
Xuất bộ flashcard ra Anki/Quizlet.

Cho phép người dùng tự nhập câu hỏi/đáp án.

Chế độ thi thử (quiz theo thời gian).

Lưu trữ dữ liệu flashcard trên server hoặc cloud.
