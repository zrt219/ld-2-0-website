export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[];

export type Database = {
  public: {
    Tables: {
      sports: {
        Row: {
          id: string;
          slug: string;
          name: string;
          is_active: boolean;
          created_at: string;
        };
        Insert: {
          id?: string;
          slug: string;
          name: string;
          is_active?: boolean;
          created_at?: string;
        };
        Update: {
          id?: string;
          slug?: string;
          name?: string;
          is_active?: boolean;
          created_at?: string;
        };
      };
      programs: {
        Row: {
          id: string;
          sport_id: string;
          slug: string;
          title: string;
          tagline: string;
          format: string;
          created_at: string;
        };
        Insert: {
          id?: string;
          sport_id: string;
          slug: string;
          title: string;
          tagline: string;
          format?: string;
          created_at?: string;
        };
        Update: {
          id?: string;
          sport_id?: string;
          slug?: string;
          title?: string;
          tagline?: string;
          format?: string;
          created_at?: string;
        };
      };
      program_versions: {
        Row: {
          id: string;
          program_id: string;
          version_semver: string;
          duration_weeks: number;
          is_active: boolean;
          created_at: string;
        };
        Insert: {
          id?: string;
          program_id: string;
          version_semver: string;
          duration_weeks?: number;
          is_active?: boolean;
          created_at?: string;
        };
        Update: {
          id?: string;
          program_id?: string;
          version_semver?: string;
          duration_weeks?: number;
          is_active?: boolean;
          created_at?: string;
        };
      };
      program_foundations: {
        Row: {
          id: string;
          program_id: string;
          foundation_number: number;
          week_number: number;
          name: string;
          subtitle: string;
          description: string;
          created_at: string;
        };
        Insert: {
          id?: string;
          program_id: string;
          foundation_number: number;
          week_number: number;
          name: string;
          subtitle: string;
          description: string;
          created_at?: string;
        };
        Update: {
          id?: string;
          program_id?: string;
          foundation_number?: number;
          week_number?: number;
          name?: string;
          subtitle?: string;
          description?: string;
          created_at?: string;
        };
      };
      performance_edge_tools: {
        Row: {
          id: string;
          slug: string;
          name: string;
          description: string;
          tool_order: number;
          created_at: string;
        };
        Insert: {
          id?: string;
          slug: string;
          name: string;
          description: string;
          tool_order: number;
          created_at?: string;
        };
        Update: {
          id?: string;
          slug?: string;
          name?: string;
          description?: string;
          tool_order?: number;
          created_at?: string;
        };
      };
      profiles: {
        Row: {
          id: string;
          email: string;
          full_name: string;
          handicap_index: string | null;
          division: string | null;
          home_club: string | null;
          pga_coach_alignment: string | null;
          is_admin: boolean;
          created_at: string;
          updated_at: string;
        };
        Insert: {
          id: string;
          email: string;
          full_name: string;
          handicap_index?: string | null;
          division?: string | null;
          home_club?: string | null;
          pga_coach_alignment?: string | null;
          is_admin?: boolean;
          created_at?: string;
          updated_at?: string;
        };
        Update: {
          id?: string;
          email?: string;
          full_name?: string;
          handicap_index?: string | null;
          division?: string | null;
          home_club?: string | null;
          pga_coach_alignment?: string | null;
          is_admin?: boolean;
          created_at?: string;
          updated_at?: string;
        };
      };
      cohorts: {
        Row: {
          id: string;
          program_id: string;
          program_version_id: string;
          organization_id: string | null;
          title: string;
          cohort_code: string;
          start_date: string;
          status: "upcoming" | "active" | "completed" | "archived";
          created_at: string;
        };
        Insert: {
          id?: string;
          program_id: string;
          program_version_id: string;
          organization_id?: string | null;
          title: string;
          cohort_code: string;
          start_date: string;
          status?: "upcoming" | "active" | "completed" | "archived";
          created_at?: string;
        };
        Update: {
          id?: string;
          program_id?: string;
          program_version_id?: string;
          organization_id?: string | null;
          title?: string;
          cohort_code?: string;
          start_date?: string;
          status?: "upcoming" | "active" | "completed" | "archived";
          created_at?: string;
        };
      };
      weekly_reflections: {
        Row: {
          id: string;
          cohort_id: string;
          week_number: number;
          profile_id: string;
          prompt_question: string;
          response_text: string;
          what_noticed: string | null;
          what_worked: string | null;
          what_repeat: string | null;
          submitted_at: string;
        };
        Insert: {
          id?: string;
          cohort_id: string;
          week_number: number;
          profile_id: string;
          prompt_question: string;
          response_text: string;
          what_noticed?: string | null;
          what_worked?: string | null;
          what_repeat?: string | null;
          submitted_at?: string;
        };
        Update: {
          id?: string;
          cohort_id?: string;
          week_number?: number;
          profile_id?: string;
          prompt_question?: string;
          response_text?: string;
          what_noticed?: string | null;
          what_worked?: string | null;
          what_repeat?: string | null;
          submitted_at?: string;
        };
      };
      performance_plans: {
        Row: {
          id: string;
          profile_id: string;
          cohort_id: string;
          pressure_signal: string | null;
          reset_protocol: string | null;
          pre_shot_cadence: Json | null;
          anchor_cue: string | null;
          goals_30_day: Json | null;
          submitted_at: string;
          updated_at: string;
        };
        Insert: {
          id?: string;
          profile_id: string;
          cohort_id: string;
          pressure_signal?: string | null;
          reset_protocol?: string | null;
          pre_shot_cadence?: Json | null;
          anchor_cue?: string | null;
          goals_30_day?: Json | null;
          submitted_at?: string;
          updated_at?: string;
        };
        Update: {
          id?: string;
          profile_id?: string;
          cohort_id?: string;
          pressure_signal?: string | null;
          reset_protocol?: string | null;
          pre_shot_cadence?: Json | null;
          anchor_cue?: string | null;
          goals_30_day?: Json | null;
          submitted_at?: string;
          updated_at?: string;
        };
      };
      mentor_reviews: {
        Row: {
          id: string;
          plan_id: string;
          reviewer_id: string;
          review_notes: string;
          review_media_url: string | null;
          reviewed_at: string;
        };
        Insert: {
          id?: string;
          plan_id: string;
          reviewer_id: string;
          review_notes: string;
          review_media_url?: string | null;
          reviewed_at?: string;
        };
        Update: {
          id?: string;
          plan_id?: string;
          reviewer_id?: string;
          review_notes?: string;
          review_media_url?: string | null;
          reviewed_at?: string;
        };
      };
    };
  };
};
