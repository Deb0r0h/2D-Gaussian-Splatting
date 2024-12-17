
"""

OPT 1

(base) flexsight@Flexsight:~/PycharmProjects/2D-Gaussian-Splatting$ export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}
(base) flexsight@Flexsight:~/PycharmProjects/2D-Gaussian-Splatting$ export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
(base) flexsight@Flexsight:~/PycharmProjects/2D-Gaussian-Splatting$ conda activate surfel_splatting


OPT 2

(base) flexsight@Flexsight:~/PycharmProjects/2D-Gaussian-Splatting$ conda activate surfel_splatting
(surfel_splatting) flexsight@Flexsight:~/PycharmProjects/2D-Gaussian-Splatting$ export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}
(surfel_splatting) flexsight@Flexsight:~/PycharmProjects/2D-Gaussian-Splatting$ export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}






 RuntimeError:
      The detected CUDA version (11.5) mismatches the version that was used to compile
      PyTorch (12.1). Please make sure to use the same CUDA versions.


(surfel_splatting) flexsight@Flexsight:~/PycharmProjects/2D-Gaussian-Splatting$ nvcc --version
    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2021 NVIDIA Corporation
    Built on Thu_Nov_18_09:45:30_PST_2021
    Cuda compilation tools, release 11.5, V11.5.119
    Build cuda_11.5.r11.5/compiler.30672275_0


export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda-12.4
export PATH=/usr/local/cuda-12.4/bin:$PATH


"""