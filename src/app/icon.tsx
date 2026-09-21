import { ImageResponse } from "next/og";

export const size = {
  width: 32,
  height: 32,
};

export const contentType = "image/png";

export default function Icon() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          backgroundColor: "#faf7f0",
          border: "2px solid #b7a891",
          borderRadius: "6px",
        }}
      >
        <span
          style={{
            fontFamily: "serif",
            fontSize: "18px",
            fontWeight: "bold",
            color: "#7f5b1d",
            lineHeight: 1,
          }}
        >
          LD
        </span>
      </div>
    ),
    {
      ...size,
    },
  );
}
