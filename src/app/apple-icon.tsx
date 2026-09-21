import { ImageResponse } from "next/og";

export const size = {
  width: 180,
  height: 180,
};

export const contentType = "image/png";

export default function AppleIcon() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          backgroundColor: "#faf7f0",
          border: "8px solid #b7a891",
          borderRadius: "36px",
          boxShadow: "inset 0 0 20px rgba(198, 165, 92, 0.25)",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            width: "120px",
            height: "120px",
            borderRadius: "60px",
            border: "2px solid #c6a55c",
            backgroundColor: "#faf7f0",
          }}
        >
          <span
            style={{
              fontFamily: "serif",
              fontSize: "64px",
              fontWeight: "bold",
              color: "#7f5b1d",
              letterSpacing: "-2px",
            }}
          >
            LD
          </span>
        </div>
      </div>
    ),
    {
      ...size,
    },
  );
}
