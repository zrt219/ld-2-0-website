"use client";

import { useState, useEffect } from "react";
import Image, { ImageProps } from "next/image";

export interface RobustImageProps extends Omit<ImageProps, "onError"> {
  fallbackSrcs?: string[];
}

export function RobustImage({
  src,
  fallbackSrcs = [],
  alt,
  ...props
}: RobustImageProps) {
  const [currentSrc, setCurrentSrc] = useState(src);
  const [fallbackIndex, setFallbackIndex] = useState(0);

  useEffect(() => {
    setCurrentSrc(src);
    setFallbackIndex(0);
  }, [src]);

  const handleError = () => {
    if (fallbackIndex < fallbackSrcs.length) {
      setCurrentSrc(fallbackSrcs[fallbackIndex]);
      setFallbackIndex((prev) => prev + 1);
    }
  };

  return (
    <Image
      {...props}
      src={currentSrc}
      alt={alt}
      onError={handleError}
    />
  );
}
