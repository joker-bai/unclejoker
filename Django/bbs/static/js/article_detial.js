$("#div_digg .action").click(function () {
    // 获取is_up的值
    let is_up = $(this).hasClass("diggit");
    // 获取文章ID
    let article_id = $(".info").attr("article_id");
    // AJAX提交
    $.ajax({
        url: "/blog/up_down/",
        type: "post",
        data: {
            csrfmiddlewaretoken: $("[name = 'csrfmiddlewaretoken']").val(),
            is_up: is_up,
            article_id: article_id,
        },
        success: function (data) {
            console.log(data.status);
            if (data.status) {
                // 如果is_up为true，在页面上点赞部分加1，反之在点踩部分加1
                if (is_up) {
                    // 获取原有的点赞数
                    let $bin = $("#digg_count");
                    let val = $bin.text();
                    val = parseInt("val") + 1;
                    console.log(val);
                    $bin.text(val);
                } else {
                    // 获取原有的点踩数
                    let $bin = $("#bury_count");
                    let val = $bin.text();
                    val = parseInt("val") + 1;
                    $bin.text(val);
                }
            } else {
                $("#digg_tips").html(data.msg);
                setTimeout(function () {
                    $("#digg_tips").html("")
                }, 2000)
            }
        }
    })
});