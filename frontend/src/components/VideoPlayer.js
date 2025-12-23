import React from "react";
import { getYouTubeId } from "../utils/youtube";

export default function VideoPlayer({ url }) {
  const videoId = getYouTubeId(url);

  if (!videoId) {
    return <p className="text-red-500">Invalid video URL</p>;
  }

  return (
    <div className="w-full aspect-video rounded-lg overflow-hidden shadow">
      <iframe
        src={`https://www.youtube.com/embed/${videoId}`}
        title="YouTube video"
        className="w-full h-full"
        allowFullScreen
      />
    </div>
  );
}
