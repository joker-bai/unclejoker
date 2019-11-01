//给提交按钮绑定事件
// 获取父评论ID
let pid = "";
// 获取article-id
let article_id = $(".info").attr("article_id");
$("#btn_comment_submit").click(function () {
    // 获取评论内容
    let content = $("#comment-content").val();
    // 如果Pid不为空，则格式化评论内容
    if (pid) {
        let index = content.indexOf("\n");
        content = content.slice(index + 1);
    }
    $.ajax({
        url: "/blog/comment/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: $("[name = 'csrfmiddlewaretoken']").val(),
            article_id: article_id,
            content: content,
            pid: pid
        },
        success: function (data) {
            console.log(data);
            let content = data.content;
            let username = data.username;

            let comment_text = '<div>\n' +
                '                <a href="">' + username + '</a>\n' +
                '            </div>\n' +
                '            <!--评论的内容 -->\n' +
                '            <div>\n' +
                '                <p class="comment-detail">' + content + '</p>\n' +
                '                <hr>\n' +
                '            </div>';
            $(".comment-list").append(comment_text);

            // 提交评论成功后，清空评论框里的内容
            $("#comment-content").val("");
        }

    })
});

//给回复按钮绑定事件
$(".replay-btn").click(function () {
    // 点击恢复按钮跳到恢复评论框
    $("#comment-content").focus();
    // 将父评论的作者写入评论框
    let author = "@" + $(this).attr("username") + "\n";
    $("#comment-content").val(author);
    pid = $(this).attr("user_pid");
});

//展示评论数
$.ajax({
    url: "/blog/comment_tree/" + article_id + '/',
    success: function (data) {
        console.log(data);
        $.each(data, function (index, comment_list) {
            pid = comment_list.parent_comment_id;
            let show_comment = "<div class=\"comment-item\" comment_id=\"" + comment_list.pk + "\">\n" +
                "        <span class=\"content\">" + comment_list.user+':'+comment_list.content + "</span>\n" +
                "    </div>";
            if (pid) {
                // 子评论
                //根据ID找到对应的评论
                $("[comment_id = " + pid + "]").append(show_comment);
            } else {
                // 根评论
                $(".comment-tree").append(show_comment);
            }
        });
    }
});