<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>sample</title>
</head>
<body>
<p><?php

for($i = 0; $i < count($_FILES["upfile"]["name"]); $i++ ){

if (is_uploaded_file($_FILES["upfile"]["tmp_name"][$i])) {
  # 名前を指定してファイル情報を取得する
	$input_file = $_FILES["upfile"];

	# 拡張子を取得する
	$file_ext = pathinfo($input_file["name"][$i], PATHINFO_EXTENSION);

	# アップロード可能な拡張子であるか調べる
	if(FileExtensionGetAllowUpload($file_ext)){

		# 現在の時間を取得する
		$time_now = time();
		# 保存先のファイルパスを生成する（実戦運用する場合、排他処理を考慮して保存先のファイル名を生成する必要があります）
		$file_name_new = "files/" . $time_now . $i . "." . $file_ext;
	
		# ファイルの移動を行う
		if(move_uploaded_file ($input_file["tmp_name"][$i], $file_name_new)){
      chmod($file_name_new,0644);
      echo ("Uploaded files<br>");
    }else{
      echo ("Failed to send files");
    }
  }else{
    echo ("Invalid files");
  }
}else{
      echo ("No file selected");
}

}
	#// -----------------------------------------------------
	#// 拡張子からアップロードを許すか調べる
	#// -----------------------------------------------------
	function FileExtensionGetAllowUpload($ext){

		# アップロードを許可したい拡張子があればここに追加
		$allow_ext = array("bmp","jpg","jpeg","png");

		foreach($allow_ext as $v){
			if ($v === $ext){
				return 1;
			}
		}

		return 0;
	}
  
?></p>
</body>
</html>