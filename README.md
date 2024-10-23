
## **1. Opencompass**
### 模型配置存放位置

`configs/models`  
- 相关脚本一般命名为`model.py` or `model_vllm.py`  即HF和Openai服务不同调用

### 数据配置存放位置
`configs/dataset_collections/`
- 存储在dataset配置的脚本

`configs/datasets/`
- 相关的数据集配置都在对应数据的目录下
  
### eval测试配置的存放位置
`configs/` 
- 相关脚本一般命名为`eval.py` or `eval_vllm.py`  即HF和Openai服务不同调用

### 环境启动
`conda activate opencompass_eval`


## **2. Omni-MATH**


### 通过部署工具部署API服务
- 这里建议使用--enable-prefix-caching(vllm)，加快性能表现，因为有重复的system prompt, lmdeploy 也有相关的参数设置

### 调用服务生成回答, 存储回答文件
`Omni-Math/reponse.py`
- 该脚本是多并发请求服务回答测评问题，可以在此修改服务地址、api_key以及prompt设置和相关的回答结果文件路径设置

### 评估模型回答
`cd ./Omni-Judge_eval`
- `gen_results` 中存放了模型回答的文件，建议使用其中的`sorted.py`，对回答文件进行排序生成`xx_sorted.json`,便于后续评估断开后可以直接根据已有结果继续评估
- `final_results` 中存放了调用评估模型的评估结果文件
- 在`omni_judge.sh`修改`input_file`和`output_file`的路径

`bash omni_judge.sh` 即可启动评估
