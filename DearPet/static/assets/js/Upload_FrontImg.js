var text_crop = "Crop the image"
var text_ok = "OK";
var text_cancel = "Cancel";
var text_del = "Are you sure to delete this photo？";
$(!function ($, window) {
    "use strict";
    const cropperCSS = document.createElement('link');
    cropperCSS.rel = 'stylesheet';
    cropperCSS.href = '/static/assets/css/cropper.min.css?v=2';
    document.head.appendChild(cropperCSS);

    const bootstrapCSS = document.createElement('link');
    bootstrapCSS.rel = 'stylesheet';
    bootstrapCSS.href = '/static/assets/css/bootstrap.css';
    document.head.appendChild(bootstrapCSS);

    const scriptCompressor = document.createElement('script');
    scriptCompressor.src = '/static/assets/js/compressor.min.js';
    document.head.appendChild(scriptCompressor);

    const scriptBootstrap = document.createElement('script');
    scriptBootstrap.src = '/static/assets/js/bootstrap.bundle.min.js';
    document.head.appendChild(scriptBootstrap);

    const scriptCropper = document.createElement('script');
    scriptCropper.src = '/static/assets/js/cropper.min.js';
    document.head.appendChild(scriptCropper);


    function FrontImg(element, options) {
        this.$element = $(element);
        this.options = $.extend({}, FrontImg.DEFAULTS, options || {});
        this.init();
    }

    FrontImg.DEFAULTS = {
        floder: 'FrontImg',
        maxnum: 1,
        width: 2.25,
        height: 4.05,
    };

    FrontImg.prototype.init = function () {
        var _this = this,
            options = _this.options;

        _this.createDOM();

        _this.AddOldPic();

        _this.BindEvent();

        //console.log(_this)
    };
    FrontImg.prototype.AddOldPic = function () {
        var _this = this;

        var OldPicStr = _this.$element.val();
        if (OldPicStr && OldPicStr.length > 0) {
            var OldPicArr = OldPicStr.split('|');
            if (OldPicArr.length > 0) {
                for (var i = 0; i < OldPicArr.length; i++) {
                    _this.AppendImg(OldPicArr[i]);
                }
            }
        }

    }

    FrontImg.prototype.CheckNum = function () {
        var _this = this;
        var imgnum = _this.$ImgBox.find("img").length;
        if (imgnum >= _this.options.maxnum) {
            //Tips("最多上传" + _this.options.maxnum + "张图片", 2);
            _this.$ImgBtn.hide();
            return false;
        } else {
            _this.$ImgBtn.show();
        }


    }
    FrontImg.prototype.AppendImg = function (imgurl) {
        var _this = this;
        _this.$ImgBtn.before('<div class="album_add imgitem"><a><img src="' + imgurl + '" /></a></div>');
        _this.$ImgBox.find(".imgitem a").css({ 'height': _this.options.height + 'rem', 'width': _this.options.width + 'rem' })
        _this.$ImgBox.find(".imgitem img").css({ 'height': (_this.options.height) + 'rem', 'width': (_this.options.width) + 'rem' })

        _this.CheckNum();

    }

    FrontImg.prototype.SetEleVal = function () {
        var _this = this;
        var imgurl = "";
        var imgs = _this.$ImgBox.find("img");
        for (var i = 0; i < imgs.length; i++) {
            var url = $(imgs[i]).attr("src");
            if (i == 0) { imgurl += url; }
            else { imgurl += "|" + url; }
        }
        _this.$element.val(imgurl);
        _this.CheckNum();


    }

    FrontImg.prototype.BindEvent = function () {
        var _this = this;

        _this.$ImgBtn.on('click.frontimg.addimg', function () {
            _this.$ImgInput.click();
        })
        _this.$ImgInput.on('change.frontimg.addimg', function () {
            _this.CheckNum();

            var files = this.files;

            var done = function (url) {
                _this.$cropperimg.src = url;
                _this.$cropperbtn.prop('disabled', false);
                _this.$modal.modal('show');
            };

            var reader;
            var file;
            var url;

            if (files && files.length > 0) {
                file = files[0];

                if (URL) {
                    done(URL.createObjectURL(file));
                } else if (FileReader) {
                    reader = new FileReader();
                    reader.onload = function (e) {
                        done(reader.result);
                    };
                    reader.readAsDataURL(file);
                }
            }
            _this.$ImgInput.val("");

        })
        _this.$cropperbtn.on('click.frontimg.crop', function () {
            _this.$cropperbtn.prop('disabled', true);
            var canvas;
            if (_this.cropper) {
                canvas = _this.cropper.getCroppedCanvas({

                    imageSmoothingEnabled: true
                });
                canvas.toBlob(function (blob) {

                    new Compressor(blob, {
                    quality: 0.8,
                    width: 960,
                    success(result) {
                        blobToDataURI(result, function (base64img) {
                            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

                            fetch('/assess_upload/', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                    'X-CSRFToken': csrfToken
                                },
                                body: JSON.stringify({
                                    img: base64img,
                                    type: 'frontupload'
                                })
                            })
                            .then(response => response.json())
                            .then(data => {
                                const imgpath = data.url;
                                console.log('Imagen subida:', data.url);
                                if (!imgpath || imgpath.length <=3) {
                                    Tips("Upload Failed：" + imgpath);
                                    return;
                                }
                                _this.AppendImg(imgpath);
                                _this.SetEleVal();
                                _this.$modal.modal('hide');
                            })
                            .catch(error => {
                                console.log('Error:', error);
                            });
                        });
                    },
                    error(e) {
                        console.log(e.message);
                    },
                });

                }, 'image/jpeg', 1);
            }

        })


        _this.$modal.on('shown.bs.modal', function () {
            _this.cropper = new Cropper(image, {
                aspectRatio: 9 / 16,
                viewMode: 2,
                rotatable: true,
                minCropBoxWidth: 200, // 设置裁剪框的最小宽度为100像素
                minCropBoxHeight: 200, // 设置裁剪框的最小高度为100像素
            });

        }).on('hidden.bs.modal', function () {
            _this.cropper.destroy();
            _this.cropper = null;
        });

        _this.$undobtn.on('click', function () {
            _this.cropper.rotate(-90);

        })
        _this.$redobtn.on('click', function () {
            _this.cropper.rotate(90);

        })

        _this.$ImgBox.on('click.frontimg.addimg', ".imgitem", function () {
            var ImgObj = this;
            TipConfirm(text_del, function () {
                var imgpath = $(ImgObj).find("img").attr("src");
                const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
                fetch('/eliminar_imagen/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                  },
                  body: JSON.stringify({
                        path: imgpath,
                         type: 'imgdel'})
                })
                .then(res => res.json())
                .then(data => {
                  if (data.success) {
                        $(ImgObj).remove();
                        _this.SetEleVal();
                    }
                    else {
                        Tip("Failed：" + data);
                         console.error("Error:", data.error)
                    }
               })
               .catch(err => console.error("Fallo:", err));
            });
        })
    }

    FrontImg.prototype.createDOM = function () {
        var _this = this;

        _this.$ImgBox = $($.parseHTML('' +
            ' <div class="ItemAss_img">' +
            '    <input type="file" accept="image/*" class="hidden">' +
            '    <div class="album_add">' +
            '        <a></a>' +
            '    </div>' +
            '  </div>'));

        _this.$modal = $($.parseHTML('' +
            '<div class="modal fade" id="modal" tabindex="-1" role="dialog" aria-labelledby="modalLabel" aria-hidden="true">' +
            '<div class="modal-dialog" role="document">' +
            '  <div class="modal-content">' +
            '    <div class="modal-header">' +
            '      <h5 class="modal-title" id="modalLabel">' + text_crop + '</h5>' +
            '      <button type="button" class="close"data-bs-dismiss="modal" aria-label="Close">' +
            '        <span aria-hidden="true">&times;</span>' +
            '      </button> ' +
            '    </div> ' +
            '    <div class="modal-body" > ' +
            '      <div class="img-container" style="max-height:400px">' +
            '        <img name="image" src="">' +
            '      </div>' +
            '    </div>' +
            '    <div class="modal-footer"> ' +
            '<div class="btn-group">                                                                                             ' +
            '    <button type="button" class="btn btn-primary undo" data-method="rotate" data-option="-45" title="Rotate Left">       ' +
            '        <span class="docs-tooltip" data-toggle="tooltip" title="" data-original-title="cropper.rotate(-45)">        ' +
            '            <span class="iconfont icon-undo"></span>                                                                    ' +
            '        </span>                                                                                                     ' +
            '    </button>                                                                                                       ' +
            '    <button type="button" class="btn btn-primary redo" data-method="rotate" data-option="45" title="Rotate Right">       ' +
            '        <span class="docs-tooltip" data-toggle="tooltip" title="" data-original-title="cropper.rotate(45)">         ' +
            '            <span class="iconfont icon-redo"></span>                                                                    ' +
            '        </span>                                                                                                     ' +
            '    </button>                                                                                                       ' +
            '</div>                                                                                                              ' +
            '      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"">' + text_cancel + '</button>   ' +
            '      <button type="button" class="btn btn-primary cropbtn">' + text_ok + '</button> ' +
            '    </div> ' +
            '  </div> ' +
            '</div> ' +
            '</div>'));



        _this.$element.hide();
        _this.$element.after(_this.$ImgBox);
        _this.$element.after(_this.$modal);
        _this.$cropperimg = _this.$modal.find("img")[0];
        _this.cropper = null;
        _this.$cropperbtn = $(_this.$modal.find(".cropbtn")[0]);
        _this.$undobtn = $(_this.$modal.find(".undo")[0]);
        _this.$redobtn = $(_this.$modal.find(".redo")[0]);


        _this.$ImgBtn = _this.$ImgBox.find(".album_add");
        _this.$ImgBtn.find("a").css({ 'width': _this.options.width + 'rem', 'height': _this.options.height + 'rem' })
        _this.$ImgInput = _this.$ImgBox.find("input");
    };

    function blobToDataURI(blob, callback) {
        var reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onload = function (e) {
            callback(e.target.result);
        }
    }
    function Plugin(option) {
        var args = Array.prototype.slice.call(arguments, 1);

        return this.each(function () {
            var $this = $(this),
                frontImg = $this.data('frontimg');

            if (!frontImg) {
                $this.data('frontimg', (frontImg = new FrontImg(this, option)));
            }

            if (typeof option == 'string') {
                frontImg[option] && frontImg[option].apply(frontImg, args);
            }
        });
    }
    $.fn.FrontImg = Plugin;
}(jQuery, window))
