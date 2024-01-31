#include <iostream>
#include "portaudio.h"

const std::string voice_folder = "voice/";
const std::string image_folder = "image/";

void audio_to_image(const char* audio_path) {

    cv::imwrite(image_folder + "decoded_image.jpg", decoded_image);
}
