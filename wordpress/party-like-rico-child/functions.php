<?php
/**
 * Party Like Rico Child Theme
 * functions.php
 *
 * Parent theme: Hello Elementor
 * Brand: Party Like Rico Promotions LLC
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/* -------------------------------------------------------
 * 1. ENQUEUE PARENT THEME + GOOGLE FONTS + CHILD STYLES
 * ----------------------------------------------------- */
add_action( 'wp_enqueue_scripts', 'plr_child_enqueue_styles', 20 );

function plr_child_enqueue_styles() {

	// 1a. Parent theme (Hello Elementor)
	wp_enqueue_style(
		'hello-elementor-style',
		get_template_directory_uri() . '/style.css',
		[],
		wp_get_theme( 'hello-elementor' )->get( 'Version' )
	);

	// 1b. Google Fonts — Montserrat + Inter
	wp_enqueue_style(
		'plr-google-fonts',
		'https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,800&family=Inter:wght@300;400;500;600;700&display=swap',
		[],
		null
	);

	// 1c. Child theme stylesheet
	wp_enqueue_style(
		'plr-child-style',
		get_stylesheet_directory_uri() . '/style.css',
		[ 'hello-elementor-style', 'plr-google-fonts' ],
		wp_get_theme()->get( 'Version' )
	);
}

/* -------------------------------------------------------
 * 2. PRECONNECT GOOGLE FONTS (Performance)
 * ----------------------------------------------------- */
add_action( 'wp_head', 'plr_preconnect_google_fonts', 1 );

function plr_preconnect_google_fonts() {
	echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
	echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
}

/* -------------------------------------------------------
 * 3. THEME SETUP
 * ----------------------------------------------------- */
add_action( 'after_setup_theme', 'plr_child_setup' );

function plr_child_setup() {

	// Allow WordPress to manage the document <title>
	add_theme_support( 'title-tag' );

	// Custom logo support
	add_theme_support( 'custom-logo', [
		'height'      => 80,
		'width'       => 220,
		'flex-height' => true,
		'flex-width'  => true,
		'header-text' => [ 'site-title', 'site-description' ],
	] );

	// Post thumbnails
	add_theme_support( 'post-thumbnails' );

	// HTML5 semantic markup
	add_theme_support( 'html5', [
		'search-form',
		'comment-form',
		'comment-list',
		'gallery',
		'caption',
		'style',
		'script',
	] );

	// Wide/full alignment for Gutenberg (if used)
	add_theme_support( 'align-wide' );

	// Responsive embeds
	add_theme_support( 'responsive-embeds' );
}

/* -------------------------------------------------------
 * 4. REGISTER NAVIGATION MENUS
 * ----------------------------------------------------- */
add_action( 'after_setup_theme', 'plr_register_menus' );

function plr_register_menus() {
	register_nav_menus( [
		'primary'        => __( 'Primary Navigation', 'party-like-rico-child' ),
		'footer-events'  => __( 'Footer — Events', 'party-like-rico-child' ),
		'footer-company' => __( 'Footer — Company', 'party-like-rico-child' ),
	] );
}

/* -------------------------------------------------------
 * 5. ELEMENTOR — REGISTER BRAND COLORS IN EDITOR PALETTE
 * ----------------------------------------------------- */
add_action( 'elementor/editor/after_enqueue_styles', 'plr_elementor_brand_palette_css' );

function plr_elementor_brand_palette_css() {
	// Push brand colors into the Elementor editor so dark bg is visible
	echo '<style>
		.elementor-editor-active body,
		#elementor-preview-iframe body { background-color: #0B0F14 !important; }
	</style>';
}

/* -------------------------------------------------------
 * 6. INJECT BRAND CSS VARIABLES INTO ELEMENTOR GLOBAL CSS
 * ----------------------------------------------------- */
add_action( 'elementor/frontend/before_enqueue_styles', 'plr_elementor_css_vars' );

function plr_elementor_css_vars() {
	// Ensures CSS variables are available even before child CSS loads
	wp_add_inline_style( 'plr-child-style', '
		:root {
			--plr-bg: #0B0F14;
			--plr-gold: #FACC15;
			--plr-green: #22C55E;
			--plr-orange: #F97316;
		}
	' );
}

/* -------------------------------------------------------
 * 7. BODY CLASSES
 * ----------------------------------------------------- */
add_filter( 'body_class', 'plr_body_classes' );

function plr_body_classes( array $classes ): array {
	$classes[] = 'plr-theme';
	if ( is_front_page() ) {
		$classes[] = 'plr-home';
	}
	return $classes;
}

/* -------------------------------------------------------
 * 8. REMOVE HELLO ELEMENTOR DEFAULT HEADER/FOOTER
 *    (Elementor Theme Builder handles these instead)
 * ----------------------------------------------------- */
add_action( 'after_setup_theme', 'plr_remove_hello_header_footer' );

function plr_remove_hello_header_footer() {
	// Remove default Hello Elementor header
	remove_action( 'hello_elementor_header', 'hello_elementor_header_markup' );
	// Remove default Hello Elementor footer
	remove_action( 'hello_elementor_footer', 'hello_elementor_footer_markup' );
}

/* -------------------------------------------------------
 * 9. DISABLE GUTENBERG ON PAGES (ELEMENTOR-ONLY)
 * ----------------------------------------------------- */
add_filter( 'use_block_editor_for_post_type', 'plr_disable_gutenberg_for_pages', 10, 2 );

function plr_disable_gutenberg_for_pages( bool $enabled, string $post_type ): bool {
	if ( 'page' === $post_type ) {
		return false;
	}
	return $enabled;
}

/* -------------------------------------------------------
 * 10. CUSTOM IMAGE SIZES
 * ----------------------------------------------------- */
add_action( 'after_setup_theme', 'plr_custom_image_sizes' );

function plr_custom_image_sizes() {
	add_image_size( 'plr-event-card',   600, 400, true );  // Event card thumbnail
	add_image_size( 'plr-hero-banner', 1920, 900, true );  // Hero full-width banner
	add_image_size( 'plr-og-image',    1200, 630, true );  // Open Graph / social share
}

/* -------------------------------------------------------
 * 11. ENQUEUE ADMIN STYLES (OPTIONAL)
 * ----------------------------------------------------- */
add_action( 'admin_enqueue_scripts', 'plr_admin_styles' );

function plr_admin_styles() {
	wp_add_inline_style( 'wp-admin', '
		#adminmenu .toplevel_page_elementor img,
		#wpadminbar .ab-item { }
		.plr-admin-badge {
			background: #FACC15;
			color: #0B0F14;
			padding: 2px 6px;
			border-radius: 4px;
			font-size: 10px;
			font-weight: 700;
		}
	' );
}
