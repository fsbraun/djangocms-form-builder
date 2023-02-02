$(function () {
    $('fieldset.action-auto-hide input[type="checkbox"][name="form_actions"]').each(function (index, element) {
        if (element.checked) {
            $("."+$(element).attr("value")).removeClass("action-hide");
        }
        $(element).on("change", function (event) {
            var element = event.target;
            if (element.checked) {
                $("." + $(element).val()).removeClass("action-hide");
            } else {
                $("." + $(element).val()).addClass("action-hide");
            }
        });
    });
});
